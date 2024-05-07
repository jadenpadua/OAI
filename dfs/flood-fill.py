class Solution:
    def isOutOfBounds(self, image, sr, sc):
        # asserts that current indecies are in range of image matrix
        return sr < 0 or sr > len(image) - 1 or sc < 0 or sc > len(image[0]) - 1

    def dfs(self, image, sr, sc, newColor, prevColor):
        # base case: invalid if not in bounds || cell != prevColor || cell == newColor
        if (
            self.isOutOfBounds(image, sr, sc)
            or image[sr][sc] != prevColor
            or image[sr][sc] == newColor
        ):
            return image
        # set current cell to new Color 
        image[sr][sc] = newColor
        # run 4D DFS to recursve through all possible directions
        self.dfs(image, sr - 1, sc, newColor, prevColor)
        self.dfs(image, sr + 1, sc, newColor, prevColor)
        self.dfs(image, sr, sc + 1, newColor, prevColor)
        self.dfs(image, sr, sc - 1, newColor, prevColor)
        # return built image at the end
        return image

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        # set prevColor to color on initial cell 
        prevColor = image[sr][sc]
        # run 4D DFS for flood fill algorithm
        res = self.dfs(image, sr, sc, color, prevColor)
        return res
