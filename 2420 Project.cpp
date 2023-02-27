//Program 4-Sorting Algorithms
//Colby Barrett


#include <iostream> /* general I/O streams */
#include <fstream>  /* file I/O */
#include <stdlib.h> /* srand, rand */
#include <time.h>   /* time for random seed */
#include <ctime>

using namespace std;

//Swap Function
void Swap(int* A, int* B) {
	int tmp;

	tmp = *A;
	*A = *B;
	*B = tmp;
}

//Partition function for quicksort
int partition(int A[], int p, int r) {
	int x = A[r];
	int i = p - 1;
	int j;
	for (j = p; j < r; j++) {
		if (A[j] <= x) {
			i = i + 1;
			Swap(&A[i], &A[j]);
		}
	}
	Swap(&A[i + 1], &A[r]);
	return i + 1;
}

//Quicksort function
void quickSort(int A[], int p, int r) {
	if (p < r) {
		int q = partition(A, p, r);
		quickSort(A, p, q - 1);
		quickSort(A, q + 1, r);
	}
}

int main(void) {
	string filename;   // name to store the generated data
	int i;// loop control variable
	int j;
	int nums;       // the number of values to store in the file
	int theNum;		// the random number (values in range 0 - 100,000,000)
	int min;
	//int* sortArray;
	int sortArraySelect[1000000] = { 0 };
	int sortArrayQuick[1000000] = { 0 };
	ifstream infile; 
	streampos begin;
	streampos end;
	streampos size;
	cout << "Please enter the name of the file to read: ";
	cin >> filename;
	infile.open(filename);
	if (!infile) {
		cerr << "Cannot find file, exiting program" << endl;
		exit(1);
	}

	begin = infile.tellg(); // get the beginning location as streampos type
	infile.seekg(0, ios::end); // go to the end of the file
	end = infile.tellg();  // get the end position of the file as streampos
	size = end - begin;  // size is number of bytes in the file
	nums = size / sizeof(int); // divide number of bytes by size of integers
	infile.seekg(0, ios::beg); // rewind, set the position of the file to beginning
	//sortArray = new int(nums);
	for (i = 0; i < nums; i++) {
		infile.read((char*)&theNum, sizeof(int));
		sortArraySelect[i] = theNum;
		sortArrayQuick[i] = theNum;
		//cout << sortArray[i] << endl;
	}

	//Selection Sort

	std::clock_t c_start = std::clock();  // start timer
	for (i = 0; i < nums - 1; i++) {
		min = i;
		for (j = i + 1; j < nums; j++) {
			if (sortArraySelect[min] > sortArraySelect[j]) {
				min = j;
			}
		}
		Swap(&sortArraySelect[i], &sortArraySelect[min]);
	}
	std::clock_t c_end = std::clock();    // end timer

	long double time_elapsed_sec = (c_end - c_start) / CLOCKS_PER_SEC;
	std::cout << "CPU time used: " << time_elapsed_sec << " sec\n";

	/*cout << "Selection Sort: " << endl;
	for (i = 0; i < nums; i++) {
		cout << sortArraySelect[i] << endl;
	}*/

	//Quick Sort

	std::clock_t c_start1 = std::clock();  // start timer

	quickSort(sortArrayQuick, 0, nums - 1);

	std::clock_t c_end1 = std::clock();    // end timer
	long double time_elapsed_sec1 = (c_end1 - c_start1) / CLOCKS_PER_SEC;
	std::cout << "CPU time used: " << time_elapsed_sec << " sec\n";

	/*cout << "Quick Sort: " << endl;
	for (i = 0; i < nums; i++) {
		cout << sortArrayQuick[i] << endl;
	}*/

	return 0;
}

