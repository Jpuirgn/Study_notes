#include "Geometry.h"
#include <cmath>

// Provided helper function
Point constructorPoints[4];
Point* updateConstructorPoints(const Point& p1,
                               const Point& p2,
                               const Point& p3,
                               const Point& p4) {
    constructorPoints[0] = p1;
    constructorPoints[1] = p2;
    constructorPoints[2] = p3;
    constructorPoints[3] = p4;
    return constructorPoints;
}

// WRITE YOUR CODE HERE...

int Polygon::numPolygons = 0;

// Rectangle Implementations
Rectangle::Rectangle(const Point& ll, const Point& ur) 
    : Polygon(updateConstructorPoints(ll, Point(ll.getX(), ur.getY()), ur, Point(ur.getX(), ll.getY())), 4) {}

Rectangle::Rectangle(int x1, int y1, int x2, int y2) 
    : Polygon(updateConstructorPoints(Point(x1, y1), Point(x1, y2), Point(x2, y2), Point(x2, y1)), 4) {}

double Rectangle::area() const {
    int width = std::abs(points.get(2)->getX() - points.get(0)->getX());
    int height = std::abs(points.get(2)->getY() - points.get(0)->getY());
    return static_cast<double>(width * height);
}

// Triangle Implementations
Triangle::Triangle(const Point& p1, const Point& p2, const Point& p3) 
    : Polygon(updateConstructorPoints(p1, p2, p3), 3) {}

double Triangle::area() const {
    const Point *p1 = points.get(0), *p2 = points.get(1), *p3 = points.get(2);
    
    // Calculate side lengths [cite: 306]
    double a = std::sqrt(std::pow(p1->getX() - p2->getX(), 2) + std::pow(p1->getY() - p2->getY(), 2));
    double b = std::sqrt(std::pow(p2->getX() - p3->getX(), 2) + std::pow(p2->getY() - p3->getY(), 2));
    double c = std::sqrt(std::pow(p3->getX() - p1->getX(), 2) + std::pow(p3->getY() - p1->getY(), 2));
    
    double s = (a + b + c) / 2.0; // Semi-perimeter [cite: 306]
    return std::sqrt(s * (s - a) * (s - b) * (s - c)); // Heron's formula [cite: 305]
}