�
��Z9  �               @   s)  d  Z  d d l Z d d l Z d d l Z d Z y? e j j e j d k rX e j	 d n
 e j	 d d d � Z
 Wn e k
 r� e �  Yn Xd	 d
 �  Z d d �  Z d d d � Z d d �  Z d d �  Z d d �  Z y e �  WnA e k
 r$Z z! d d l Z e j e d � WYd d Z [ Xn Xd S)zE
request_email.py
requests the user's email address for bug reports.
�    Na�  you can enter your email
address here, and if the game crahses,
it should be reported to me,
and I can get back to you and 
try and get it fixed!

(it is completely optional,
press 'skip' to continue)
if you dont get it, it means you didnt enter the correct email address.
contact me at <michaelveenstra12@gmail.com> for help if you do that

you should recieve a confirmation email :)
oh yeah, I wont sell it to anyone either�nt�USERPROFILE�HOMEz.stickman_new_worldZ	useremailc                 s�  t  d � i  � t j j t � r& d  St j �  � � j d d � � j d � � j	 d � � j
 d � f d d �  � t j � d	 d
 ��  �  j d d d d d d � �  j d d  d d � t j � d	 t �}  |  j d d  d d � t j � d	 d d � f d d �  �} | j d d d d � | j �  t j � d	 d d �  � � f d d �  �} | j d d d d � | j �  x[ t  d � � j d � r�d  S� j d � r�t � � t � � � j �  n  � j �  q�Wd  S)N�hi�defaultzemail_icon.icozemail addressZ250x270ZWM_DELETE_WINDOWc                  s
   t  �  � S)N)�exit� )�	variablesr   �@C:\Users\Michael\Desktop\project\terrain_viewer\request_email.py�<lambda>%   s    zmain.<locals>.<lambda>�textzemail:�anchor�centerZrelxg      �?Zrely�fill�expandT�skip�commandc                  s   t  �  d � S)NT)r   r   )r	   r   r
   r   .   s    �x��   �y�d   �donec                  s   t  �  � � � S)N)�get_textr   )�entry�rootr	   r   r
   r   2   s    ��   �quit�
entry_data)�print�os�path�exists�FILE�tkZTkZ
iconbitmap�titleZgeometry�protocolZEntry�place�packZLabel�MESSAGEZButton�get�remember�send_confirmZdestroy�update)�labelr   r   r   )r   r   r	   r
   �main   s:    
'
-



r.   c             C   s$   t  |  j �  � |  j �  | d <d  S)Nr   )r   r)   )r   r	   r   r   r   r
   r   B   s    r   Fc          	   C   s9   | r+ t  t � � } | j d � Wd  QXn  d |  d <d  S)N� Tr   )�openr"   �write)�v�save�openfiler   r   r
   r   F   s    r   c          
   C   s7   t  t d � � } | j |  d � Wd  QXt |  � d  S)N�wr   )r0   r"   r1   r   )�itemr4   r   r   r
   r*   L   s    r*   c       
   
   C   s  d d  l  } d d  l } d d l m } d } |  d g } d j t �  �  } d j t �  �  } | j d d � } | | j � j | j	 � j
 �  }	 | j �  | j | |	 � y* | j | | | � | j | | | � Wn t j j d	 d
 � Yn X| j �  d  S)Nr   )�Fernetzbugreporter.smr@mail.comr   a�  To: <{reciever}>
From: <{sender}>
Subject: confirmation email


Hi! if you are recieving this email, it means you have successfully
gotten your email address to me. Since you didn't give your password,
you shouldnt have any troubles. I will only use this when I have a very important
thing to tell you, or if the game crashes on your computer, I will be alerted
and try to fix the problem and tell you about it as well. Thanks!

zDTo: <{sender}>
From: <{reciever}>
Subject: email gotten


{reciever}zsmtp.mail.comi�  �ErrorzqThere was an error sending the email.
if this problem persists please contact me at <michaelveenstra12@gmail.com>)�smtplib�	bugreportZcryptography.fernetr7   �format�localsZSMTP_SSLZHIUEFWILEIURFHEZdecryptZFYUKYFVKFYVHUFL�decodeZehloZloginZsendmail�tkinterZ
messageboxZ	showerror�close)
�itemsr9   r:   r7   ZsenderZreciever�message�otherZserver�ar   r   r
   r+   Q   s"    !
r+   c               C   s
   t  � d  S)N)�
SystemExitr   r   r   r
   �wrong_osw   s    rE   zin request_email)�__doc__r>   r#   Ztkinter.messageboxr   r(   r    �join�name�environr"   �KeyErrorrE   r.   r   r   r*   r+   �	Exception�er:   Zdefault_smrr   r   r   r
   �<module>   s&   ?(&