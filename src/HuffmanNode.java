import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.*;

class Huffman {
    static class HuffmanNode {
        char ch;
        int freq;
        HuffmanNode left, right;

        HuffmanNode(char ch, int freq) {
            this.ch = ch;
            this.freq = freq;
            this.left = this.right = null;
        }
    }


    static class HuffmanComparator implements Comparator<HuffmanNode> {
        public int compare(HuffmanNode a, HuffmanNode b) {

            return a.freq - b.freq;
        }
    }

    private HuffmanNode root;
    private Map<Character, String> huffmanCodes = new HashMap<>();
    private Map<String, Character> reverseHuffmanCodes = new HashMap<>();

    public Map<Character, Integer> createMap(String filePath) {

        Map<Character, Integer> letterFrequency = new HashMap<>();

        try (FileInputStream fis = new FileInputStream(filePath)) {
            int byteData;
            while ((byteData = fis.read()) != -1) {
                char ch = (char) byteData;
                if (Character.isLetter(ch)) {
                    letterFrequency.put(ch, letterFrequency.getOrDefault(ch, 0) + 1);
                }
            }
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
        return letterFrequency;
    }

    public void buildTree(Map<Character, Integer> letterFrequency) {

        PriorityQueue<HuffmanNode> pq = new PriorityQueue<>(new HuffmanComparator());

        for (Map.Entry<Character, Integer> entry : letterFrequency.entrySet()) {
            pq.add(new HuffmanNode(entry.getKey(), entry.getValue()));
        }

        while (pq.size() > 1) {
            HuffmanNode left = pq.poll();
            HuffmanNode right = pq.poll();

            HuffmanNode newNode = new HuffmanNode('\0', left.freq + right.freq);
            newNode.left = left;
            newNode.right = right;

            pq.add(newNode);
        }

        root = pq.poll();
    }

    private void generateCodes(HuffmanNode node, String code) {
        if (node == null) return;

        if (node.ch != '\0') {
            huffmanCodes.put(node.ch, code);
            reverseHuffmanCodes.put(code, node.ch);
        }

        generateCodes(node.left, code + "0");
        generateCodes(node.right, code + "1");
    }

    private String encodeFile(String filePath) throws IOException {
        StringBuilder encodedData = new StringBuilder();
        try (FileInputStream fis = new FileInputStream(filePath)) {
            int byteData;
            while ((byteData = fis.read()) != -1) {
                char ch = (char) byteData;
                encodedData.append(huffmanCodes.get(ch));
            }
        }
        return encodedData.toString();
    }

    private void writeEncodedFile(String encodedData, String outputPath) throws IOException {
        try (FileOutputStream fos = new FileOutputStream(outputPath)) {
            byte[] outputBytes = encodedData.getBytes();
            fos.write(outputBytes);
        }
    }

    public String generate_decode(String encodeData){
        StringBuilder decodedString = new StringBuilder();
        String currentCode = "";


        for (char bit : encodeData.toCharArray()) {
            currentCode += bit;


            if (reverseHuffmanCodes.containsKey(currentCode)) {
                decodedString.append(reverseHuffmanCodes.get(currentCode));
                currentCode = "";
            }
        }

        return decodedString.toString();
    }
    public void writeDecodeFile(String decodedString, String outputPath) throws IOException {
        try (FileOutputStream fos = new FileOutputStream(outputPath)) {
            byte[] outputBytes = decodedString.getBytes();
            fos.write(outputBytes);
        }
    }


    //main
    public void DecodeAnEncode(String inputFilePath, String encodePath, String decodePath) throws IOException {
        // Create frequency map
        Map<Character, Integer> freqMap = createMap(inputFilePath);

        // Build the Huffman Tree
        buildTree(freqMap);

        // Generate Huffman Codes
        generateCodes(root, "");


        // Encode the input file
        String encodedData = encodeFile(inputFilePath);

        // Write encoded data to output file
        writeEncodedFile(encodedData, encodePath);


        String decodedData = generate_decode(encodedData);

        // Write decoded data to output file
        writeDecodeFile(decodedData, decodePath);

    }


    public static void main(String[] args) {
        Huffman encoder = new Huffman();
        try {
            encoder.DecodeAnEncode("C:\\Users\\User\\IdeaProjects\\huffman\\src\\input.txt",
                    "C:\\Users\\User\\IdeaProjects\\huffman\\src\\output.txt",
                    "C:\\Users\\User\\IdeaProjects\\huffman\\src\\output_decode.txt");
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }}







