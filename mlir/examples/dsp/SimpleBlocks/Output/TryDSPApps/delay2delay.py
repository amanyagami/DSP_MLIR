
def main() {

  #size 10
  var a10 = [ 10,20,30,40,50,60,70,80,90,100];

  var delay1 = 3;
  var delay2 = 4;
  var y1 = delay(a10, delay1);
  var y2 = delay(y1, delay2);;
  
  # Get fft 
  
  # var c = a10 + a10;
  # var d = c + c;
  # var e = slidingWindowAvg(d);
  # var g1 = downsampling(a10 , 2);
  # var f = upsampling(a10, 8);
  # var g = downsampling(f , 4);
  # var g<8> = downsampling(f , 2);
  # var h<15> = FIRFilter(g,g);
  # var e = delay(c, d);
  # var f = e[0];
  print(y2);
  # print(d);
  # print(e);

}

