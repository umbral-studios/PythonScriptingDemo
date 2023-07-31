#pragma once

#include "CoreMinimal.h"
#include "DA_Item.h"
#include "Engine/DataAsset.h"
#include "DA_ShopItem.generated.h"

/**
 * 
 */
UCLASS()
class PYTHONSCRIPTINGDEMO_API UDA_ShopItem : public UPrimaryDataAsset
{
	GENERATED_BODY()

public:
	UPROPERTY(BlueprintReadWrite, EditAnywhere)
	UDA_Item* Item;

	UPROPERTY(BlueprintReadWrite, EditAnywhere)
	int Cost;

	UFUNCTION(BlueprintCallable)
	UDA_Item* GetItemByName(const FString ItemName)
	{
		return FindObject<UDA_Item>(ANY_PACKAGE, *ItemName);
	}
	
};
