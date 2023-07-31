import unreal

ASSET_TOOLS = unreal.AssetToolsHelpers.get_asset_tools()
ASSET_FACTORY = unreal.DataAssetFactory()


def create_item(item_name: str):
    new_item = ASSET_TOOLS.create_asset(
        f"DA_Item_{item_name}",
        "/Game/Items",
        unreal.DA_Item,
        ASSET_FACTORY
    )

    new_item.name = item_name
    new_item.set_rarity(3)

    unreal.EditorAssetLibrary.save_loaded_asset(new_item)
    
print("CREATING ITEMS")
create_item(item_name="Sword")

