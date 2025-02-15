
import java.util.Scanner;

public class CeaserCipher{
	public static String ceaser_cipher(  String text , int shift  , char action) {
	
		String result = "";
		
		for (int i = 0 ; i < text.length() ; i++)
		{
			char ch = text.charAt(i);
			
			if (Character.isLetter(ch)) {
				
				char base = Character.isLowerCase(ch) ? 'a': 'A';
				
				int  shiftvalue = (action == 'e') ? shift : -shift;
				
				int newChar = (ch - base + shiftvalue ) % 26;
				
				if (newChar < 0) {
					
					newChar += 26;
					
				}
				
				result += (char) (base + newChar);
			}
			
			else {
				
				result += ch ;
			}
		}	
		return result;
	}
	public static void main(String[] args) {
		
		Scanner s = new Scanner(System.in);
		
		
		System.out.println("Enter the e for Encryption and d for Decryption : ");
		char action = s.next().toLowerCase().charAt(0);
		
		while (action == 'e' && action == 'd') {
			System.out.println("Please select valid option e for Encryption or d for Decryption");
			action = s.next().toLowerCase().charAt(0);
			
		}
		
		s.nextLine();
		System.out.print("Enter text message : ");
		String text = s.nextLine();
		
	
		System.out.println("Enter the shift value : ");
		int shift = s.nextInt();
		
		String result = ceaser_cipher( text , shift , action );
		System.out.println("Your new form is : " + result);	
		
	}
}