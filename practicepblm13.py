{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b572457c-f2ad-4973-9f47-2bd43364d8d4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 22\n",
      " 85\n",
      " Sports\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "14040.0\n"
     ]
    }
   ],
   "source": [
    "\n",
    "age=int(input().strip())\n",
    "health_score=int(input().strip())\n",
    "vehicle_type=input().strip()\n",
    "\n",
    "base_price=10000\n",
    "f_price=0\n",
    "\n",
    "if age<25:\n",
    "    f_price=base_price+ base_price*(20/100)\n",
    "elif age>50:\n",
    "    f_price=base_price+ base_price*(15/100)\n",
    "else:\n",
    "    f_price=base_price \n",
    "\n",
    "\n",
    "if health_score>=80:\n",
    "    f_price=f_price-f_price*(10/100)\n",
    "elif health_score<60:\n",
    "    f_price=f_price+f_price*(20/100)\n",
    "else:\n",
    "     f_price=f_price\n",
    "\n",
    "if vehicle_type==\"Sports Car\" or \"Sports\":\n",
    "    f_price=f_price+f_price*(30/100)\n",
    "elif vehicle_type==\"SUV\":\n",
    "    f_price=f_price+f_price*(15/100)  \n",
    "else:\n",
    "     f_price=f_price \n",
    "\n",
    "print(f_price)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "00ce33fd-484a-45be-86bb-2f95c0c8593f",
   "metadata": {},
   "outputs": [],
   "source": []
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
