
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class IpRegex {

    public static void main(String[] args) {

        String patternStr = "^((000|[0-9]|[0-9][0-9]|[0-1][0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[0-9][0-9]|[0-1][0-9]{2}|2[0-4][0-9]|25[0-5])$";
        Pattern pattern = Pattern.compile(patternStr);

        String input = "this fails";

        // create a matcher that will match the given input against this pattern
        Matcher matcher = pattern.matcher(input);

        boolean matchFound = matcher.matches();
        System.out.println(input + " - matches: " + matchFound);

        input = "121.234.12.12";
        // reset the matcher with a new input sequence
        matcher.reset(input);
        matchFound = matcher.matches();
        System.out.println(input + " - matches: " + matchFound);

        // Attempts to match the input sequence, starting at the beginning
        // of the region, against the pattern
        matchFound = matcher.lookingAt();
        System.out.println(input + " - matches from the beginning: " + matchFound);

    }

}