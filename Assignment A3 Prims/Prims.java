class PrimsMST{
    // Number of vertices in the graph
    int vertexCount = 5;
    
    int minKeyIndex(int vertex[], Boolean visited[]){

        int minimum = Integer.MAX_VALUE;
        int min_index = -1;

        for(int i=0; i< vertexCount; i++){
            if(visited[i] == false && vertex[i] < minimum){
                min_index = i;
                minimum = vertex[i];
            }
        }
        return min_index;
    }

    void printPrimsMST(int parent[], int graph[][]){
        System.out.println("Edge \t  Weight");
        int weight =0;
        for(int i=1; i<vertexCount; i++){
            System.out.println(parent[i]+" - "+i+" \t\t"+graph[i][parent[i]]);
            weight += graph[i][parent[i]];
        }
        System.out.println("Total Weight : "+weight);
    }

    void primsAlgo(int graph[][]){
        int parent[] = new int[vertexCount];            // Array to store constructed MST
        int vertex[] = new int[vertexCount];            // Key values used to pick minimum weight edge in cut
        Boolean visited[] = new Boolean[vertexCount];   // To represent set of vertices included in MST
        
        for(int i=0; i< vertexCount; i++){              // Initialize all keys as INFINITE
            vertex[i] = Integer.MAX_VALUE;
            visited[i] = false;
        }

        vertex[0] = 0;  // set vertex 0 to 0 so as to select first vertex
        parent[0] = -1; // ?
        
        for(int i=0; i < vertexCount-1; i++){   //
            int minVertexIndex = minKeyIndex(vertex, visited);
            visited[minVertexIndex] = true;

            for(int v= 0; v < vertexCount; v++){
                if(graph[minVertexIndex][v] != 0 && visited[v] == false && graph[minVertexIndex][v] < vertex[v]){
                    parent[v] = minVertexIndex;
                    vertex[v] = graph[minVertexIndex][v];
                }
            }
        }
        
        printPrimsMST(parent,graph);
    }
    
}
class Prims{
    public static void main(String args[]){
        System.out.println("Prim's Minimal Spanning Tree Algorithm");
        int graph[][] = {
        //   A  B  C  D  E
            {0, 0, 3, 0, 0},    //A  
            {0, 0, 10, 4, 0},   //B
            {3, 10, 0, 2, 6},   //C 
            {0, 4, 2, 0, 1},    //D
            {0, 0, 6, 1, 0},    //E
        };

        PrimsMST primsMST = new PrimsMST();
        primsMST.primsAlgo(graph);
    }
}


/*
    B-----10----C-----3-----A
    |         / /
    |       /  /
    4     2   6
    |   /    /
    | /     /
    D---1---E

*/
