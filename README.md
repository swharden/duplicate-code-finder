# Duplicate Code Finder
A simple Python script to identify duplicate lines in the code base of any programming language

_TIP: duplications are more accurate if an autoformatter is used throughout the whole code base._

## Sample Output

```
Count   Code
-----   --------------------------------------------------
113     Worksheet wks = Project.ActiveLayer();
53      LT_execute(LTCommand);
51      GraphLayer gL;
47      Tree tr;
44      WorksheetPage wksPg;
40      if(!wks){
39      pCLAMPSweep mySweep;
39      pCLAMPFile myABF(cc_GetPath());
38      GraphLayer gL = Project.ActiveLayer();
34      " ty -b "
34      LT_execute(
31      " ");
30      string LTCommand;
27      GraphPage gP;
26      iNumberOfOutputCols++;
24      wks.GetParent(wksPg);
23      vColLabels[iColOffset] = strLabel;
23      TreeNode tnDefaults;
21      if(verbose){
21      GETN_CHECKBOX_BRANCH(0)
21      iColor = 1;
21      DWORD dwBegin = GetTickCount();
20      Tree GetTree;
20      Worksheet wks;
18      if(bAbsVal)wksOut.Columns(iCol - 1).SetComments(" abs()");
18      tr.GetN.ID = 1;
17      if(bRet){
17      GraphLayer gl = Project.ActiveLayer();
17      iNumParametersPerStim++;
16      gL.GetParent(gP);
16      DWORD dwEnd = GetTickCount();
16      if(!cc_GetABFGraph_and_Settings(gL, tnDefaults))return;
15      trNode = tr.GetN;
15      TreeNode trNode;
15      Dataset dsTemp;
14      if(cc_NotAnABF(myABF))return;
13      wksIn.Columns(iCol - 1).SetUnits(" ms ");
13      if(gL){
13      TreeNode tn;
12      foreach(Layer wksLayer in wksPg.Layers){
12      printf(" \n ");
12      bGetSlopeStats = true;
11      LTCommand.Format(" lay -s %i; " , i);
11      iColor = 2;
11      DataRange dr;
11      string strLabel;
11      vector<string> vFilePaths;
10      mResults[iCount++][iCol][iRange] = 9E6;
10      if(loop > 1){
10      for(j = 1; j < = loop; j++){
10      int loop, j;
10      GETN_SEPARATOR_LINE
10      tnGetTree = GetTree.GetN;
10      TreeNode tnGetTree;
10      Folder fld = Application.ActiveFolder();
10      for(int i = 0; i < wks.GetNumCols(); i++){
10      } catch(int iErr){
10      Dataset dsX, dsY;
```