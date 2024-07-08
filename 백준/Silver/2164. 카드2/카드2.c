#include <stdio.h>
#include <stdlib.h>
#define MAX_QUEUE 500001

typedef enum
{
    false,
    true
} bool;
typedef int Data;

typedef struct
{
    int front, rear;
    Data items[MAX_QUEUE];
} Queue;

void InitQueue(Queue *pqueue)
{
    pqueue->front = pqueue->rear = 0;
}

bool IsFull(Queue *pqueue)
{
    return pqueue->front == (pqueue->rear + 1) % MAX_QUEUE;
}

bool IsEmpty(Queue *pqueue)
{
    return pqueue->front == pqueue->rear;
}

void EnQueue(Queue *pqueue, Data item)
{
    if (IsFull(pqueue))
        return;
    pqueue->items[pqueue->rear] = item;
    pqueue->rear = (pqueue->rear + 1) % MAX_QUEUE;
}

Data DeQueue(Queue *pqueue)
{
    if (IsEmpty(pqueue))
        return -1;
    Data item = pqueue->items[pqueue->front];
    pqueue->front = (pqueue->front + 1) % MAX_QUEUE;
    return item;
}

int main()
{
    Queue queue;
    InitQueue(&queue);
    int num = 0;

    int n;
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
    {
        EnQueue(&queue, i);
    }

    while (!IsEmpty(&queue))
    {
        num = DeQueue(&queue);
        if (IsEmpty(&queue))
            break;
        num = DeQueue(&queue);
        EnQueue(&queue, num);
    }
    printf("%d", num);

    return 0;
}