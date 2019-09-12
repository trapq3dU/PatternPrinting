{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number of rows you want to print \n",
      "5\n",
      "\n",
      "\n",
      "X\n",
      "X\n",
      "\n",
      "\n",
      "OX\n",
      "OX\n",
      "\n",
      "\n",
      "XOX\n",
      "XOX\n",
      "\n",
      "\n",
      "OXOX\n",
      "OXOX\n",
      "\n",
      "\n",
      "XOXOX\n",
      "XOXOX\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "l=[]\n",
    "print(\"Enter the number of rows you want to print \")\n",
    "n=int(input())\n",
    "for i in range(0,n+1):\n",
    "    check=i\n",
    "    while(check!=0):\n",
    "        for j in range (0,i):\n",
    "            if(check%2==0):\n",
    "                l.append(\"O\")\n",
    "                check-=1\n",
    "            else:\n",
    "                l.append(\"X\")\n",
    "                check-=1\n",
    "        \n",
    "        #print(i,\"......\")        \n",
    "        for x in range(0,2):\n",
    "            for k in l:                \n",
    "                print(k,end='')\n",
    "            print('\\n',end='')\n",
    "        \n",
    "        \n",
    "        \n",
    "    l=[]\n",
    "    print(\"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
