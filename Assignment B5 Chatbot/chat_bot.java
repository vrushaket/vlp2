
import javax.swing.JOptionPane;
import java.sql.*;
import java.util.Scanner;

public class chat_bot {
    public static void main(String args[]) {
        ss1 s = new ss1();
    }
};

class ss1 extends javax.swing.JFrame {
    public ss1() {
        initComponents();
        this.setVisible(true);
        status.setVisible(true);
    }

    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        jTextField1 = new javax.swing.JTextField();
        jButton1 = new javax.swing.JButton();
        jScrollPane1 = new javax.swing.JScrollPane();
        chatArea = new javax.swing.JTextArea();
        jLabel2 = new javax.swing.JLabel();
        status = new javax.swing.JLabel();
        jLabel1 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setResizable(false);

        jPanel1.setBackground(new java.awt.Color(97, 1, 0));
        jPanel1.setForeground(new java.awt.Color(229, 119, 131));
        jPanel1.setLayout(null);

        jTextField1.setToolTipText("text\tType your message here...");
        jTextField1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                // jTextField1ActionPerformed(evt);
            }
        });
        jPanel1.add(jTextField1);
        jTextField1.setBounds(10, 370, 410, 40);

        jButton1.setBackground(new java.awt.Color(229, 119, 131));
        jButton1.setFont(new java.awt.Font("Tahoma", 1, 11)); // NOI18N
        jButton1.setText("Send");
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {

                try {
                    Class.forName("com.mysql.cj.jdbc.Driver");
                    Connection con = DriverManager.getConnection(
                            "jdbc:mysql://db4free.net:3306/amarchatbot?characterEncoding=latin1",
                            "amarchatbot", "amarchatbot");
                    Statement stmt = con.createStatement();
                    String query = jTextField1.getText().toString();
                    chatArea.append("Me : " + query + "\n");
                    if (query.equalsIgnoreCase("bye")) {
                        setVisible(false);
                        dispose();
                    }
                    ResultSet rs = stmt.executeQuery("SELECT answer FROM `chatbot` WHERE query='" + query + "'");
                    if (rs.next()) {
                        String res = rs.getString(1);

                        chatArea.append("Bot : " + res + "\n");
                    } else {
                        System.out.println("Bot : Sorry! unable to answer.");
                        chatArea.append("Bot : Sorry! unable to answer.\n");
                    }
                    jTextField1.setText("");
                    con.close();
                } catch (Exception e) {
                    System.out.println(e);
                }

            }
        });
        jPanel1.add(jButton1);
        jButton1.setBounds(420, 370, 80, 40);

        chatArea.setColumns(20);
        chatArea.setRows(5);
        jScrollPane1.setViewportView(chatArea);

        jPanel1.add(jScrollPane1);
        jScrollPane1.setBounds(10, 80, 490, 280);

        jLabel2.setFont(new java.awt.Font("Myriad Pro", 1, 38)); // NOI18N
        jLabel2.setForeground(new java.awt.Color(255, 255, 255));
        jLabel2.setText("Chatbot");
        jPanel1.add(jLabel2);
        jLabel2.setBounds(140, 20, 180, 40);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
                layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                        .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, 508,
                                javax.swing.GroupLayout.PREFERRED_SIZE));
        layout.setVerticalGroup(
                layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                        .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, 419,
                                javax.swing.GroupLayout.PREFERRED_SIZE));

        setSize(new java.awt.Dimension(508, 441));
        setLocationRelativeTo(null);
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JTextArea chatArea;
    private javax.swing.JButton jButton1;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JTextField jTextField1;
    private javax.swing.JLabel status;
    // End of variables declaration//GEN-END:variables
}
