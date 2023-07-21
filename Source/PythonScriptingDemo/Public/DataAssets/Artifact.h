#pragma once

#include "CoreMinimal.h"
#include "Engine/DataAsset.h"
#include "PythonScriptingDemo/PythonScriptingDemo.h"
#include "Artifact.generated.h"

UCLASS()
class PYTHONSCRIPTINGDEMO_API UArtifact : public UPrimaryDataAsset
{
	GENERATED_BODY()

public:
	UPROPERTY(BlueprintReadWrite, EditAnywhere)
	FName Name;

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

	UFUNCTION(BlueprintCallable, Category = "Artifact")
	ERarity GetRarity() const
	{
		return Rarity;
	}
};
