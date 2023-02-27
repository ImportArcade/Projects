#pragma once
class Matrix
{
private:
	int nrows = 0;
	int ncols = 0;
	double** array = nullptr;
public:
	Matrix(int r, int c);
	Matrix mult(const Matrix m) const;
	void read();
	void print(int width = 6);
};

