package model;

import observer.ArenaObserver;
import entity.Cell;

import java.util.Vector;

public class Arena {
	private static final Arena arena = new Arena();
    public final int WIDTH = 20;
    public final int HEIGHT = 15;
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
        if( 0 <= cell.x && cell.x < WIDTH && 0 <= cell.y && cell.y < HEIGHT){
            //System.out.println(" "+cell.x+" "+WIDTH+" "+cell.y+" "+HEIGHT);
            return true;
        }
        else{
            return false;
        }
    }     
}
