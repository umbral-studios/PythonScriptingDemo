#pragma once

#include "CoreMinimal.h"
#include "Artifact.h"
#include "Engine/DataAsset.h"
#include "ShopItem.generated.h"

UCLASS()
class PYTHONSCRIPTINGDEMO_API UShopItem : public UPrimaryDataAsset
{
	GENERATED_BODY()

public:
	UPROPERTY(BlueprintReadWrite, EditAnywhere)
	UArtifact* Artifact;

	UPROPERTY(BlueprintReadWrite, EditAnywhere)
	int Cost;

	UFUNCTION(BlueprintCallable, Category = "ShopItem")
	UArtifact* GetArtifactByName(const FString ArtifactName)
	{
		return FindObject<UArtifact>(ANY_PACKAGE, *ArtifactName);
	}
};
