# test-repositoryvoid setup() { 
  size(640, 360, P3D);
  noStroke();  
} 
 

void draw() {
  
  lights();
  
  background(0, 0, 26);
  translate(width/2, height/2); 
  
  for(int i = 0; i < num; i++) {
    float gray = map(i, 0, num-1, 0, 255);
    pushMatrix();
    fill(gray);
    rotateY(a + offset*i);
    rotateX(a/2 + offset*i);
    box(200);
    popMatrix();
  }
  
  a += 0.01;    
}
