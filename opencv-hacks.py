#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing opencv-python library
import cv2


# In[9]:


import numpy


# Own Pic

# In[11]:


own_pic=numpy.zeros((147,147,3))


# In[15]:


#violet
own_pic[0:21,0:147]=[255,0,127]
own_pic[0:147,0:21]=[255,0,127]


# In[16]:


#Indigo
own_pic[22:42,22:147]=[130,0,75]
own_pic[22:147,22:42]=[130,0,75]


# In[17]:


#Blue
own_pic[43:63,43:147]=[255,0,0]
own_pic[43:147,43:63]=[255,0,0]


# In[18]:


#Green
own_pic[64:84,64:147]=[0,128,0]
own_pic[64:147,64:84]=[0,128,0]


# In[19]:


#Yellow
own_pic[85:105,85:147]=[0,255,255]
own_pic[85:147,85:105]=[0,255,255]


# In[20]:


#Orange
own_pic[106:126,106:147]=[0,140,255]
own_pic[106:147,106:126]=[0,140,255]


# In[21]:


#Red
own_pic[127:147,127:147]=[0,0,255]
own_pic[127:147,127:147]=[0,0,255]


# In[22]:


cv2.imshow("my photo",own_pic)
cv2.waitKey()
cv2.destroyAllWindows()


# Cropping two images and swapping them

# In[ ]:


pic1=cv2.imread('pic22.jpg')


# In[ ]:


pic2=cv2.imread('pic2.png')


# In[4]:


pic1.shape


# In[5]:


pic2.shape


# In[26]:


crop1=pic1[120:420,50:450]


# In[27]:


crop2=pic2[120:420,50:450]


# In[28]:


temp_pic1=numpy.copy(pic1)


# In[29]:


temp_pic2=numpy.copy(pic2)


# In[30]:


temp_pic1[120:420,50:450]=crop2


# In[31]:


temp_pic2[120:420,50:450]=crop1


# In[ ]:


cv2.imshow("my photo",temp_pic1)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:


cv2.imshow("my photo",temp_pic2)
cv2.waitKey()
cv2.destroyAllWindows()


# Collage

# In[33]:


crop3=numpy.hstack((temp_pic1,temp_pic2))


# In[34]:


cv2.imshow("my photo",crop3)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:




