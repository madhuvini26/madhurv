int size = list.length;
while (size > 0)
{ 
  int min = Integer.MAX_VALUE; 
  for (int i = 0; i < size; i++) 
  { 
    int temp = queue.dequeue(); 
    if (temp < min) min = temp;
    queue.enqueue(temp);
    }
  for (int i = 0; i < size; i++)
  { 
    int temp = queue.dequeue();
    if (temp == min) break; 
    queue.enqueue(temp);
  }
  stack.push(min); 
  size--;  
}
