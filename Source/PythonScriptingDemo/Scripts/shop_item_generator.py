import enum
import unreal

ASSET_TOOLS = unreal.AssetToolsHelpers.get_asset_tools()
ASSET_FACTORY = unreal.DataAssetFactory()


class ERarity(enum.Enum):
    Common = 0
    Uncommon = 1
    Rare = 2
    Legendary = 3


RARITY_COST_MAP = {
    ERarity.Common.value: 100,
    ERarity.Uncommon.value: 150,
    ERarity.Rare.value: 300,
    ERarity.Legendary.value: 1000
}


def create_shop_item(item_name: str):
    new_item = ASSET_TOOLS.create_asset(
        f"DA_Shop_{item_name}",
        "/Game/ShopItems",
        unreal.DA_ShopItem,
        ASSET_FACTORY
    )

    new_item.item = new_item.get_item_by_name(f"DA_Item_{item_name}")
    new_item.cost = RARITY_COST_MAP[new_item.item.get_rarity().value]
    unreal.EditorAssetLibrary.save_loaded_asset(new_item)


print("CREATING SHOP ITEMS")
create_shop_item(item_name="Sword")
create_shop_item(item_name="Hammer")
create_shop_item(item_name="Shield")
