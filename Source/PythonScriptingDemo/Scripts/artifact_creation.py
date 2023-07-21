import unreal
from enum import Enum

# =========== CONSTANTS ================
OUTPUT_DIR = "/Game"  # where to store the data assets we create
ARTIFACT_ASSET_CLASS = unreal.Artifact  # the asset we are trying to create
SHOP_ITEM_ASSET_CLASS = unreal.ShopItem  # the asset we are trying to create
ASSET_FACTORY = unreal.DataAssetFactory()  # a factory to create data assets
ASSET_TOOLS = unreal.AssetToolsHelpers.get_asset_tools()


# declare a python version of the enum so they're compatible
class ERarity(Enum):
    COMMON = 0
    UNCOMMON = 1
    RARE = 2
    Legendary = 3


# lets say we want each rarity to always have a specific cost
RARITY_COST_VALUES = {
    ERarity.COMMON.value: 50,
    ERarity.UNCOMMON.value: 100,
    ERarity.RARE.value: 200,
    ERarity.Legendary.value: 400,
}


def create_artifact(asset_name: str, rarity: ERarity):
    # create the asset
    new_artifact = ASSET_TOOLS.create_asset(
        f"Artifact_{asset_name}",
        f"{OUTPUT_DIR}/Artifacts",
        ARTIFACT_ASSET_CLASS,
        ASSET_FACTORY
    )

    # update the properties
    new_artifact.name = asset_name
    new_artifact.set_rarity(rarity.value)

    # then save the asset
    unreal.EditorAssetLibrary.save_loaded_asset(new_artifact)


def create_shop_item(artifact_asset_name: str):
    # create the asset
    new_shop_item = ASSET_TOOLS.create_asset(
        f"ShopItem_{artifact_asset_name}",
        f"{OUTPUT_DIR}/ShopItems",
        SHOP_ITEM_ASSET_CLASS,
        ASSET_FACTORY
    )

    # get the artifact we want linked to this item

    # OPTION 1: get the artifact by name
    artifact = new_shop_item.get_artifact_by_name(f"ARTIFACT_{artifact_asset_name}")
    # OPTION 2: pass in the pointer to the artifact you create directly

    # update the properties
    new_shop_item.artifact = artifact
    new_shop_item.cost = RARITY_COST_VALUES[artifact.get_rarity().value]

    # then save the asset
    unreal.EditorAssetLibrary.save_loaded_asset(new_shop_item)


def create_shop_items(artifact_dir: str):
    assets = unreal.EditorAssetLibrary.list_assets(artifact_dir)
    for asset in assets:
        artifact_name = asset.split(".")[-1].replace("Artifact_", "")
        create_shop_item(artifact_name)


artifact = create_artifact("Cube", ERarity.Legendary)
create_shop_items(f"{OUTPUT_DIR}/Artifacts")
