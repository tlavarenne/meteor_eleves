#!/usr/bin/octave -qf
pkg load communications;
arg_list = argv ();
phrase = arg_list{1};
[decoded,e]=viterbi([1 1 1 1 0 0 1; 1 0 1 1 0 1 1] ,phrase,0);
ddd=(decoded(1:4:end)*8+decoded(2:4:end)*4+decoded(3:4:end)*2+decoded(4:4:end));
dddd=dec2hex(ddd)';
save output.txt dddd ;
save error.txt e;
