class Solution{
    public long inversionCount(int  arr[]){
        int N = arr.length;
        int n = (int)N;
        int[] temp = new int[n];
        return sortSubarray(arr, temp, 0, n - 1);
    }
    private long sortSubarray(int arr[], int temp[], int low, int high){
        int res = 0;
        if(low < high){
            int mid = low + (high - low) / 2;
            res += sortSubarray(arr, temp, low, mid);
            res += sortSubarray(arr, temp, mid + 1, high);
            res += mergeSubarray(arr, temp, low, mid, high);
        }
        return res;
    }
    private int mergeSubarray(int arr[], int temp[], int low, int mid, int high){
        for(int i = low; i <= high; i++){
            temp[i] = arr[i];
        }
        int i = low;
        int j = mid + 1;
        int k = low;
        int res = 0;
        while(i <= mid && j <= high){
            if(temp[i] <= temp[j]){
                arr[k] = temp[i];
                i++;
            }else{
                arr[k] = temp[j];
                j++;
                res += (mid - i + 1);
            }
            k++;
        }
        while(i <= mid){
            arr[k] = temp[i];
            k++;
            i++;
        }
        while(j <= high){
            arr[k] = temp[j];
            k++;
            j++;
        }
        return res;
    }
}