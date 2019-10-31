import java.awt.*;  
import java.awt.event.*;  
class Action extends Frame implements ActionListener{  
TextField t;  
public Action(){  
  
t=new TextField();  
t.setBounds(60,50,250,20);  
Button b=new Button("click me");  
b.setBounds(100,120,80,30);  
  

b.addActionListener(this);
  

add(b);
add(t);  
setSize(500,500);  
setLayout(null);  
setVisible(true);  
}  
public void actionPerformed(ActionEvent e){  
t.setText("HELLO,THERE!!!!!!!!!!!!!!!!!");  
}  
public static void main(String args[]){  
 Action a=new Action();  
}  
}  