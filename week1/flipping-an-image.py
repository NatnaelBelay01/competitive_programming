class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for idx in range(len(image)):
            image[idx] = image[idx][::-1]
        print(image)
        
        for row in range(len(image)):
            for col in range(len(image[0])):
                if (image[row][col] == 1):
                    image[row][col] = 0
                else:
                    image[row][col] = 1
        return image