# -*- coding=utf-8 -*-


def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n//2
    print(gap)

    while gap > 0:
        for i in range(gap, n):
            j = i
            # 插入排序
            while j > 0:
                if alist[j] < alist[j-gap]:
                    alist[j], alist[j-gap] = alist[j-gap], alist[j]
                    j -= gap
                else:
                    break
        gap //= 2


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    shell_sort(li)
    print(li)