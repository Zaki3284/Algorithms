#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;

    // Constructor
    ListNode(int x) {
        val = x;
        next = NULL;
    }
};

void intilase(){

    ListNode* l1 = new ListNode(2);
    l1->next = new ListNode(4);
    l1->next->next = new ListNode(3);

    ListNode* l2 = new ListNode(5);
    l2->next = new ListNode(6);
    l2->next->next = new ListNode(4);

    ListNode* l3;
}


void insert(ListNode*& l3, int number) {
    ListNode* newNode = new ListNode(number);

    // إذا كانت القائمة فارغة
    if (l3 == NULL) {
        l3 = newNode;
        return;
    }

    // نذهب إلى آخر عنصر
    ListNode* temp = l3;
    while (temp->next != NULL) {
        temp = temp->next;
    }

    // نربط العقدة الجديدة في النهاية
    temp->next = newNode;
}

void AddTwoNumbers(ListNode* l1, ListNode* l2)
{
    ListNode* tmp1 = l1;
    ListNode* tmp2 = l2;
    ListNode* l3 = NULL;
    


    while (tmp1 != NULL || tmp2 != NULL)
    {
        if (tmp1 != NULL && tmp2 !=NULL)
        {
            cout << tmp1->val;
            tmp1 = tmp1->next;
            tmp2 = tmp2->next;
            insert(l3, tmp1->val + tmp2->val);
        }
        else
        {
            cout << " ";
        }


        
    }
}
int main() {

AddTwoNumbers(l1, l2);
    return 0;
}