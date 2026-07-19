#include <iostream>
#include <queue>
using namespace std;

struct Node {
    char ch;
    int freq;
    Node *left, *right;

    Node(char c, int f) {
        ch = c;
        freq = f;
        left = right = NULL;
    }

    Node(Node *l, Node *r) {
        ch = '\0';
        freq = l->freq + r->freq;
        left = l;
        right = r;
    }
};

struct Compare {
    bool operator()(Node *a, Node *b) {
        return a->freq > b->freq;
    }
};

void printCodes(Node *root, string code) {
    if (!root)
        return;

    if (!root->left && !root->right)
        cout << root->ch << " : " << code << endl;

    printCodes(root->left, code + "0");
    printCodes(root->right, code + "1");
}

int main() {
    char ch[] = {'A', 'B', 'C', 'D', 'E', 'F'};
    int freq[] = {5, 9, 17, 13, 16, 40};
    int n = 6;

    priority_queue<Node*, vector<Node*>, Compare> pq;

    for (int i = 0; i < n; i++)
        pq.push(new Node(ch[i], freq[i]));

    while (pq.size() > 1) {
        Node *left = pq.top();
        pq.pop();

        Node *right = pq.top();
        pq.pop();

        Node *parent = new Node(left, right);
        pq.push(parent);
    }

    Node *root = pq.top();

    cout << "Huffman Codes:\n";
    printCodes(root, "");

    return 0;
}
