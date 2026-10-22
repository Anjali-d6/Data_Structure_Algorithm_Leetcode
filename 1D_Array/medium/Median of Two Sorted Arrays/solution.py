def findMedianSortedArrays(nums1, nums2):
    i = 0
    j = 0
    merged = []

    
    while i < len(nums1) and j < len(nums2):

        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Add remaining elements from nums1
    while i < len(nums1):
        merged.append(nums1[i])
        i += 1

    # Add remaining elements from nums2
    while j < len(nums2):
        merged.append(nums2[j])
        j += 1

    # Find median
    n = len(merged)

    if n % 2 == 1:
        return float(merged[n // 2])
    else:
        middle1 = n // 2 - 1
        middle2 = n // 2

        return (merged[middle1] + merged[middle2]) / 2