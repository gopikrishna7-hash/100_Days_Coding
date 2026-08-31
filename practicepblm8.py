{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "056eb220-80eb-444a-aead-643910d08da5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 10\n",
      " 1 6 3 9 3 10 23 22 2 5\n",
      " 5\n",
      " 3 24 6 2 8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11\n"
     ]
    }
   ],
   "source": [
    "# union()\n",
    "\n",
    "# The .union() operator returns the union of a set and the set of elements in an iterable.\n",
    "# Sometimes, the | operator is used in place of .union() operator, but it operates only on the set of elements in set.\n",
    "# Set is immutable to the .union() operation (or | operation).\n",
    "\n",
    "eng_len=int(input())\n",
    "eng_set=set(map(int,input().split()))\n",
    "fre_len=int(input())\n",
    "fre_set=set(map(int,input().split()))\n",
    "res=eng_set.union(fre_set)\n",
    "\n",
    "print(len(res))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
