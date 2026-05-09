# CNN model
model = S e q u e n ti al ( [
Embedding ( v o c a b si z e , 1 2 8 , i n p u t l e n g t h=max len ) ,
Conv1D ( 1 2 8 , 5 , a c t i v a t i o n =’ r el u ’ ) ,
GlobalMaxPooling1D ( ) ,
Dense ( 6 4 , a c t i v a t i o n =’ r el u ’ ) ,
Dense ( v o c a b si z e , a c t i v a t i o n =’ so ftmax ’ )
] )
model . c ompile ( o p timi z e r =’adam ’ , l o s s =’ s p a r s e c a t e g o r i c a l c r o s s e n t r o p y ’ )
# Train
model . f i t (X, y [ : , 0 ] , ep och s =10)
p r i n t ( ”CNN model t r ai n e d s u c c e s s f u l l y ” )
# LSTM Model
import numpy a s np
from t e n s o r fl o w . k e r a s . l a y e r s import LSTM
# Reuse same t o k e n i z e r and data from above
model = S e q u e n ti al ( [
Embedding ( v o c a b si z e , 1 2 8 , i n p u t l e n g t h=max len ) ,
LSTM( 1 2 8 ) ,
Dense ( 6 4 , a c t i v a t i o n =’ r el u ’ ) ,
Dense ( v o c a b si z e , a c t i v a t i o n =’ so ftmax ’ )
] )
model . c ompile ( o p timi z e r =’adam ’ , l o s s =’ s p a r s e c a t e g o r i c a l c r o s s e n t r o p y ’ )
# Train
5
model . f i t (X, y [ : , 0 ] , ep och s =10)
p r i n t ( ”LSTM model t r ai n e d s u c c e s s f u l l y ” ) s
