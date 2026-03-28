#include <iostream>
#include <string>

#include "Geometry.h"

void printAttributes(Polygon* p, const std::string& name) {
    // WRITE YOUR CODE HERE...

    

    std::cout << "\n--- " << name << " Attributes ---" << std::endl;
    std::cout << "Area: " << p->area() << std::endl;
    std::cout << "Number of sides: " << p->getNumSides() << std::endl;
    std::cout << "Vertex coordinates:" << std::endl;
    const PointArray* pa = p->getPoints();
    for (int i = 0; i < p->getNumSides(); ++i){
        const Point* point = pa->get(i);
        std::cout << "  Vertex " << i + 1 << ": (" << point->getX() << ", "
                  << point->getY() << ")" << std::endl;
    }
}

 // TODO: Write a small program (a main function) that does the following:
    // - Enter the name of the shape to create, it can be one of the following:
    //   "rectangle", "triangle" (1 mark).
    //   - In the case of "rectangle", prompt for the lower-left and upper-right
    //     positions of a Rectangle and create a Rectangle object accordingly,
    //     then call printAttributes(…) on the object (4 marks)
    //   - In the case of "triangle", prompt for the 3-point positions and
    //     create a Triangle object accordingly,
    //     then call printAttributes on the object (4 marks)
    //   - In the case of other invalid shape name,
    //     print message "Invalid shape" and exit. (1 mark)
int main() {
   
    std::cout << "Enter shape name: ";

    std::string shape_name;
    std::cin >> shape_name;

    if (shape_name == "triangle") {
        std::cout << "Enter triangle coordinates: ";
        int x1, y1, x2, y2, x3, y3;
        std::cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
        Triangle tri(Point(x1, y1), Point(x2, y2), Point(x3, y3));
        printAttributes(&tri, "Triangle");
    } else if (shape_name == "rectangle") {
        std::cout << "Enter rectangle coordinates: ";
        int x1, y1, x2, y2;
        std::cin >> x1 >> y1 >> x2 >> y2;
        Rectangle rect(Point(x1, y1), Point(x2, y2));
        printAttributes(&rect, "Rectangle");
    } else {
        std::cout << "Invalid shape name" << std::endl;
    }

    return 0;

}

// # Sample Input/Output
//
// ## Sample Run 1
// Enter shape name: rectangle
// Enter rectangle coordinates: 2 3 6 3
// --- Rectangle Attributes ---
// Area: 12
// Number of sides: 4
// Vertex coordinates:
//   Vertex 1: (2, 3)
//   Vertex 2: (2, 6)
//   Vertex 3: (6, 6)
//   Vertex 4: (6, 3)
//
// ## Sample Run 2
// Enter shape name: triangle
// Enter triangle coordinates: 0 0 3 0 0 4
// --- Triangle Attributes ---
// Area: 6
// Number of sides: 3
// Vertex coordinates:
//   Vertex 1: (0, 0)
//   Vertex 2: (3, 0)
//   Vertex 3: (0, 4)
//
// ## Sample Run 3
// Enter shape name: pentagon
// Invalid shape name
