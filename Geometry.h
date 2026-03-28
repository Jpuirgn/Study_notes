#include <iostream>
#include "PointArray.h"

// Forward declarations of classes to implement
class Polygon;
class Triangle;
class Rectangle;

// Method to implement:
Point* updateConstructorPoints(const Point& p1,
                               const Point& p2,
                               const Point& p3,
                               const Point& p4 = Point(0, 0));

// WRITE YOUR CODE HERE...
#ifndef GEOMETRY_H
#define GEOMETRY_H

class Polygon {
protected:
    PointArray points;
    static int numPolygons;

public:
    // Constructor using array of Points and length [cite: 253]
    Polygon(const Point pts[], int len) : points(pts, len) {
        numPolygons++;
    }

    // Constructor using existing PointArray [cite: 256]
    Polygon(const PointArray& pa) : points(pa) {
        numPolygons++;
    }

    virtual ~Polygon() {
        numPolygons--;
    }

    virtual double area() const = 0; // Pure virtual [cite: 264]
    
    static int getNumPolygons() { return numPolygons; }
    int getNumSides() const { return points.getSize(); }
    const PointArray* getPoints() const { return &points; }
};

class Rectangle : public Polygon {
public:
    Rectangle(const Point& lowerLeft, const Point& upperRight);
    Rectangle(int x1, int y1, int x2, int y2);
    virtual double area() const override;
};

class Triangle : public Polygon {
public:
    Triangle(const Point& p1, const Point& p2, const Point& p3);
    virtual double area() const override;
};

#endif
