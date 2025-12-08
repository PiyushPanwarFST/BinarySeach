class Solution {
  public:
    long long  missingNum(vector<int>& arr) {
    int n = arr.size() + 1;
    vector<int> hash(n + 1, 0);
    for (int i = 0; i < n - 1; i++) {
        hash[arr[i]]++;
    }
    for (int i = 1; i <= n; i++) {
        if (hash[i] == 0) {
            return i;
        }
    }
    return -1;
    }
};