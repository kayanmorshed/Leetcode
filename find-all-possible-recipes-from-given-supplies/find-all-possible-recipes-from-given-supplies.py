class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)       
        result = set()
        
        for i in range(len(recipes)):
            for j in range(len(recipes)):
                flag = 1
                
                # check whether all necessary ingredients are available 
                for ingredient in ingredients[j]:
                    if ingredient not in supplies:
                        flag = 0 # ingredient not available yet
                        break

                # when all ingredients are available, add the recipe itself as the future supply
                if flag == 1:
                    result.add(recipes[j])
                    supplies.add(recipes[j])
        
        return list(result)