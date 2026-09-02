{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9a3aba29-e966-4ac1-abb2-8fb45c0f849c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " Bussiness\n",
      " 40\n",
      " True\n",
      " 65\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6426.0\n"
     ]
    }
   ],
   "source": [
    "seat_type=input().strip()\n",
    "booking_days=int(input().strip())\n",
    "festival=bool(input().strip())\n",
    "age=int(input().strip()\n",
    "i_price=5000\n",
    "f_price=0\n",
    "\n",
    "\n",
    "if seat_type==\"Bussiness\":\n",
    "    f_price=i_price+ i_price*(40/100)\n",
    "elif seat_type==\"Premium Economy\":\n",
    "    f_price=i_price+ i_price*(20/100)\n",
    "else:\n",
    "    f_price=i_price\n",
    "\n",
    "if booking_days > 30:\n",
    "    f_price= f_price-f_price*(10/100)\n",
    "elif Booking_days <7:\n",
    "    f_price=  f_price+f_price*(10/100)\n",
    "\n",
    "if festival:\n",
    "    f_price=f_price+ f_price*(20/100)\n",
    "\n",
    "if age>60:\n",
    "    f_price=f_price- f_price*(15/100)\n",
    "\n",
    "print(f_price)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b95d2aa1-47fd-4224-8b80-15d20d85730c",
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
