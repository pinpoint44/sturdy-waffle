import javax.swing.JOptionPane;

public class Fibbonaci {
    public static void main(String[] args) {
    
    String again;

    do{
    //input a nonnegative number
    int limit = Integer.parseInt(JOptionPane.showInputDialog("Enter a Number: ")); 

    int first = 0, second = 1;
            String series = "Fibonacci Series: ";  //hold values

            while (first <= limit) {
                series += first + " ";   //append current value to the string
                int next = first + second;
                first = second;
                second = next;
             
        }

    JOptionPane.showMessageDialog(null, series);  
    
    //input again?
        again = JOptionPane.showInputDialog("Do you want to input another number (y/n)");
        } while (again != null && again.equalsIgnoreCase("y")); {
         JOptionPane.showMessageDialog(null, "Thank you the program has ended!");
    }
    
  } 
}
