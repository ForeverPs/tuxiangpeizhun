import cv2
import numpy as np
import matplotlib.pyplot as plt


class Point_matching(object):

	def __init__(self):
		self.fixed = cv2.imread('Image A.jpg',cv2.IMREAD_GRAYSCALE)
		self.moving = cv2.imread('Image B.jpg',cv2.IMREAD_GRAYSCALE)

	def get_point(self):
		plt.figure('Point Matching')
		plt.subplot(1,2,1)
		plt.imshow(self.fixed,cmap='gray')
		plt.subplot(1,2,2)
		plt.imshow(self.moving,cmap='gray')
		pos = plt.ginput(15)
		print(pos)

	def Matching(self):
		P = np.matrix([[0.89544053, 1.98928931, 1.84460032, 0.88965298, 0.90122810, 0.62921279, 1.02855441],
						[1.95319667, 2.02843495, 1.00403690, 0.27480439, 1.24711441, 1.39759096, 1.24711441],
						[1, 1, 1, 1, 1, 1, 1]])
		Q = np.matrix([[1.36597088, 2.44246944, 2.04067773, 0.94143624, 1.19160844, 0.97176014, 1.31290405],
						[2.36890899, 2.16422265, 1.20901970, 0.75416115, 1.69420215, 1.90646947, 1.65629727],
						[1, 1, 1, 1, 1, 1, 1]])
		H = Q * P.T * (P * P.T).I
		print(H.I)
		m, n = np.shape(self.moving)
		new = np.zeros((m, n))
		for i in range(m):
			for j in range(n):
				co = H * np.matrix([i, j, 1]).T
				# use the same way convert [i, j] into P
				xx = int(co[0,0])
				yy = int(co[1,0])
				if xx > 0 and yy > 0 and xx < m and yy < n:
					new[i, j] = self.moving[xx, yy]
		plt.figure('Results')
		plt.subplot(1,2,1)
		plt.imshow(self.fixed,cmap='gray')
		plt.title('Original Image')
		plt.subplot(1,2,2)
		plt.imshow(new,cmap='gray')
		plt.title('Matching Result')
		plt.show()

if __name__ == '__main__':
	h = Point_matching()
#	h.get_point()
	h.Matching()
