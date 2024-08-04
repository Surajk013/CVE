#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool csv_to_excel(const string& csv_file, const string& excel_file) {
    ifstream file_in(csv_file);
    if (!file_in.is_open()) {
        cerr << "Failed to open CSV file: " << csv_file << endl;
        return false;
    }

    ofstream file_out(excel_file, ios::out | ios::binary);
    if (!file_out.is_open()) {
        cerr << "Failed to create Excel file: " << excel_file << endl;
        file_in.close();
        return false;
    }

    string line;
    while (getline(file_in, line)) {
        file_out << line << "\n";
    }

    file_in.close();
    file_out.close();
    return true;
}

int main() {
    string csv_file = "csv_data.csv";
    string excel_file = "data.xlsx";

    if (csv_to_excel(csv_file, excel_file)) {
        cout << "CSV file '" << csv_file << "' has been converted to Excel file '" << excel_file << "'" << endl;
    } else {
        cout << "Failed to convert CSV file to Excel file" << endl;
    }

    return 0;
}