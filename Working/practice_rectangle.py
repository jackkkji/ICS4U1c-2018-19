class Rectangle(object):
    def _int_(self):
        self.width = 0
        self.height = 0


def main():
    rect1 = Rectangle()
    rect1.width = int(input())
    rect1.height = int(input())
    print("The width is " + str(rect1.width))
    print("The height is " + str(rect1.height))
    print("The area is " + str(get_area(rect1)))


def get_area(rect):
    return rect.width * rect.height


main()
