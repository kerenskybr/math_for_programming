from vector_drawing import *

dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), 
                    (-4,4), (-5,3), (-5,2), (-2,2), (-5,1), 
                    (-4,0), (-2,1), (-1,0), (0,-3), (-1,-4), 
                    (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
                    ]

def exercise_1():
    # Exercise 2.3
    draw(Points(*dino_vectors))

    # Exercise 2.4
    draw(Points(*dino_vectors), Polygon(*dino_vectors))

    #Exercise 2.1
    draw(Arrow((2, -2), (0,0)))

    # Exercise 2.5
    # My answer
    points_y = [y ** 2 for y in range(-10, 11)]
    points_x = [x for x in range(-10, 11)]

    new_list = list(zip(points_x, points_y))
    draw(Points(*new_list), grid=(1,10), nice_aspect_ratio=False)

    # Book answer
    draw(Points(*[(x,x**2) for x in range(-10,11)]), grid=(1,10), nice_aspect_ratio=False)

def exercises_2():
    dino_vectors2 = translate((-1.5,-2.5), dino_vectors)
    # draw(
    #     Points(*dino_vectors, color=blue),
    #     Polygon(*dino_vectors, color=blue),
    #     Points(*dino_vectors2, color=red),
    #     Polygon(*dino_vectors2, color=red)
    #     )

    # Exercise 2.19
    from random import uniform
    u = (-1,1)
    v = (1,1)
    def random_r():
        return uniform(-3,3)
    def random_s():
        return uniform(-1,1)
    possibilities = [add(scale(random_r(), u), scale(random_s(), v)) for i in range(0,500)]
    
    draw(Points(*possibilities))

    # Exercise 2.26
    for n in range(-12,15):
        for m in range(-14, 13):
            if distance((n,m), (1,-1)) == 13 and n > m > 0:
                print((n,m))

def hundred_copies():
    translations = [(12*x,10*y) for x in range(-5,5) for y in range(-5,5)]
    dinos = [Polygon(*translate(t, dino_vectors),color=blue) for t in translations]
    draw(*dinos, grid=None, axes=None, origin=None)

if __name__ == "__main__":
    #exercise_1()
    exercises_2()
    #hundred_copies()


