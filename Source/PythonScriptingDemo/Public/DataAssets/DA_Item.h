#pragma once

#include "CoreMinimal.h"
#include "Engine/DataAsset.h"
#include "DA_Item.generated.h"

UENUM()
enum ERarity
{
	Common UMETA(DislayName = "Common"),
	Uncommon UMETA(DislayName = "Uncommon"),
	Rare UMETA(DislayName = "Rare"),
	Legendary UMETA(DislayName = "Legendary")
};

/**
 * 
 */
UCLASS()
class PYTHONSCRIPTINGDEMO_API UDA_Item : public UPrimaryDataAsset
{
	GENERATED_BODY()

public:
	UPROPERTY(BlueprintReadWrite, EditAnywhere)
	FName Name;

	UPROPERTY(BlueprintReadWrite, EditAnywhere)
	TEnumAsByte<ERarity> Rarity;

	UFUNCTION(BlueprintCallable)
	void SetRarity(int NewRarity)
	{
		if(NewRarity >= 0 && NewRarity <= (int32)ERarity::Legendary)
		{
			Rarity = static_cast<ERarity>(NewRarity);
		}
	}
	
	UFUNCTION(BlueprintCallable)
	ERarity GetRarity()
	{
		return Rarity;
	}
};
