import unreal
from enum import Enum

# =========== CONSTANTS ================
OUTPUT_DIR = "/Game/DataAssets"  # where to store the data assets we create
ASSET_CLASS = unreal.Artifact  # the asset we are trying to create
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


def create_data_asset(asset_name: str, rarity: ERarity):
    # create the asset
    asset = ASSET_TOOLS.create_asset(f"Artifact_{asset_name}", OUTPUT_DIR, ASSET_CLASS, ASSET_FACTORY)

    # update the properties
    asset.name = asset_name
    asset.set_rarity(rarity.value)
    asset.cost = RARITY_COST_VALUES[rarity.value]

    # then save the asset
    unreal.EditorAssetLibrary.save_loaded_asset(asset)


create_data_asset("Cube", ERarity.Legendary)
