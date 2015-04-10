package model;

import observer.ArenaObserver;
import entity.Cell;

import java.util.Vector;

public class Arena {
	private static final Arena arena = new Arena();
    public final int WIDTH = 20;
    public final int HEIGHT = 15;
    
    public static final int UP = 0;
	public static final int RIGHT = 1;
	public static final int DOWN = 2;
	public static final int LEFT = 3;
	
	public static int[] puzzle;
	
    private Vector<Cell> emptyCells;
    private Vector<Cell> obstacleCells;
     
    private Arena() {
        emptyCells = new Vector<Cell>();
        obstacleCells = new Vector<Cell>();
    }
     
    public static Arena getInstance() {
        return arena;
    }
 
    public Vector<Cell> getEmptyCells() {
        return emptyCells;
    }
 
    public void setEmptyCells(Vector<Cell> emptyCells) {
        this.emptyCells = emptyCells;
         
    }
 
    public Vector<Cell> getObstacleCells() {
        return obstacleCells;
    }
 
    public void setObstacleCells(Vector<Cell> obstacleCells) {
        this.obstacleCells = obstacleCells;
    }    
     
    public void addEmptyCell(Cell cell) {
        emptyCells.add(cell);
        ArenaObserver.getInstance().noticeView();
    }
     
    public void addObstacleCell(Cell cell) {
        obstacleCells.add(cell);
        ArenaObserver.getInstance().noticeView();
    }
     
    public boolean insideArena(Cell cell) {
        ///if( 0 <= cell.x && cell.x < WIDTH && 0 <= cell.y && cell.y < HEIGHT){
        if( 1 <= cell.x && cell.x <= WIDTH && 1 <= cell.y && cell.y <= HEIGHT){
            //System.out.println(" "+cell.x+" "+WIDTH+" "+cell.y+" "+HEIGHT);
            return true;
        }
        else{
            return false;
        }
    }
    
    public boolean checkObstacles(Cell newCell) {
    	
    	for (int deltaY = -1; deltaY <= 1; deltaY++)
	    {
	        for (int deltaX = -1; deltaX <= 1; deltaX++) 
	        {
	            //if (Arena.getInstance().getObstacleCells().contains(new Cell(cell.x + deltaX, cell.y +deltaY)))
	            if(puzzle[(newCell.y-1+deltaY) * WIDTH + (newCell.x-1+deltaX)] == 1)
	        	{
	                return true;
	            }
	        }
	    }
    	
    	return false;
    }
}
