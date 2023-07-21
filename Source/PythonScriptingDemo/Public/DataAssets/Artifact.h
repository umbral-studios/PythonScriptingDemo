#pragma once

#include "CoreMinimal.h"
#include "Engine/DataAsset.h"
#include "Artifact.generated.h"

UENUM(BlueprintType)
enum ERarity
{
	Common UMETA(DisplayName = "Common"),
	Uncommon UMETA(DisplayName = "Uncommon"),
	Rare UMETA(DisplayName = "Rare"),
	Legendary UMETA(DisplayName = "Legendary"),
};

UCLASS()
class PYTHONSCRIPTINGDEMO_API UArtifact : public UPrimaryDataAsset
{
	GENERATED_BODY()

public:
	UPROPERTY(BlueprintReadWrite, EditAnywhere)
	FName Name;

	UPROPERTY(BlueprintReadWrite, EditAnywhere)
	int32 Cost;

	UPROPERTY(BlueprintReadWrite, EditAnywhere)
	TEnumAsByte<ERarity> Rarity;

	UFUNCTION(BlueprintCallable, Category = "Artifact")
	void SetRarity(int NewRarity)
	{
		if (NewRarity >= 0 && NewRarity <= (int32)ERarity::Legendary)
		{
			Rarity = static_cast<ERarity>(NewRarity);
		}
	}
};
