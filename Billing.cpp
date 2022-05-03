#include <iostream>
#include <string>
#include <iomanip>
#include <string>

using namespace::std;    

struct menuItemType
{
    char menuItem[20];
    double menuPrice;
};

void getData(menuItemType menuList[8]);
void showMenu(menuItemType menuList[8], menuItemType orderList[], int orderCounter, int selection);
void printCheck(menuItemType menuList[8], int orderCounter, const double TAX);

const int MAX = 8;
const double TAX = 1.05;

menuItemType menuList[8];
menuItemType orderList[MAX];

int main()
{
    int orderCounter = 0;
    int selection = ' ';



    getData(menuList);
    showMenu(menuList, orderList, orderCounter, selection);
    printCheck(orderList, orderCounter, TAX);

return 0;
}

void getData(menuItemType menuList[8])
{

strcpy(menuList[0].menuItem,"Plain Egg");
menuList[0].menuPrice = 1.45;
strcpy(menuList[1].menuItem,"Bacon and Egg");
menuList[1].menuPrice = 2.45;
strcpy(menuList[2].menuItem,"Muffin");
menuList[2].menuPrice = 0.99;
strcpy(menuList[3].menuItem,"French Toast");
menuList[3].menuPrice = 1.99;
strcpy(menuList[4].menuItem,"Fruit Basket");
menuList[4].menuPrice = 2.49;
strcpy(menuList[5].menuItem,"Cereal");
menuList[5].menuPrice = 0.69;
strcpy(menuList[6].menuItem,"Coffee");
menuList[6].menuPrice = 0.50;
strcpy(menuList[7].menuItem,"Tea");
menuList[7].menuPrice = 0.75;

}

void showMenu(menuItemType menuList[8], menuItemType orderList[], int orderCounter, int selection)
{
cout << "1 - Plain Egg" << setw(14) << "$1.45" << endl;
cout << "2 - Bacon and Egg" << setw(10) << "$2.45" << endl;
cout << "3 - Muffin" << setw(17) << "$0.99" << endl;
cout << "4 - French Toast" << setw(11) << "$1.99" << endl;
cout << "5 - Fruit Basket" << setw(11) << "$2.49" << endl;
cout << "6 - Cereal" << setw(17) << "$0.69" << endl;
cout << "7 - Coffee" << setw(17) << "$0.50" << endl;
cout << "8 - Tea" << setw(21) << "$0.75\n" << endl;
do{
    cout << "Enter the number of your selection until you have completed your order." << endl;
    cout << "Enter 9 when you have finished." << endl;
    cin >> selection;

    switch(selection)
    {
        case 9:
        break;
        case 1:
        cout << menuList[0].menuItem << setw(14) << "$1.45";
        break;
        case 2:
        cout << menuList[1].menuItem << setw(10) << "$2.45";
        break;
        case 3:
        cout << menuList[2].menuItem << setw(17) << "$0.99";
        break;
        case 4:
        cout << menuList[3].menuItem << setw(11) << "$1.99";
        break;
        case 5:
        cout << menuList[4].menuItem << setw(11) << "$2.49";
        break;
        case 6:
        cout << menuList[5].menuItem << setw(17) << "$0.69";
        break;
        case 7:
        cout << menuList[6].menuItem << setw(17) << "$0.50";
        break;
        case 8:
        cout << menuList[7].menuItem << setw(20) << "$0.75";
        break;
        default:
        cout << "Invalid Selection! Selections must be between 1 and 9\n";
    }
}while (selection !=9);
    if((selection >=0) && (selection <= MAX))
    {
    strcpy(orderList[orderCounter].menuItem, menuList[selection-1].menuItem);
    orderList[orderCounter].menuPrice = menuList[selection-1].menuPrice;
    orderCounter++;
    }
    else if (selection == 9)
    cout << "Exit" << endl;
    else
    cout << "Invalid Entry" << endl;

}


void printCheck(menuItemType orderList[], int orderCounter, const double TAX)
{
    cout << "Welcome to the Breakfast Place!"<< endl;

    for (orderCounter = 0; orderCounter < MAX; orderCounter++)
    cout << orderList[orderCounter].menuItem << " "<< orderList[orderCounter].menuPrice<< endl;
    cout << "Tax" << setw(10) << TAX<<endl;
    cout << "Amount Due" << setw(10) << endl;
    

}