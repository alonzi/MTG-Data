{
 ////////////////////////////////////////////////////////////////////////////
 //                                                                        //
 //   who: Pete Alonzi (lpa2a@virginia.edu)                                //
 //  what: rootlogon file   (~/.rootlogon.C)                               //
 //  when: last update: 2009_June_11                                       // 
 // where: galileo.phys.virginia.edu                                       //
 //   why: change the default root canvas to acceptable configuration      //
 //                                                                        //
 // This file is run when you open root.                                   //
 // Just place it in your home directory and it works automatically.       // 
 // If you make a change to this file simply start                         //
 // a new root session and the changes will be implemented.                //
 //                                                                        //
 // If you did not install roofit then there will be an error              //
 // message when you login, it can be ignored.                             //     
 //                                                                        //
 ////////////////////////////////////////////////////////////////////////////

 // Definition of new styles
 TStyle *Nab_collaboration      = new TStyle("Nab_Collaboration","How Nab_Collaboration likes it");
 TStyle *Nab_collaboration_work = new TStyle("Nab_Collaboration_Work","How Nab_Collaboration likes it with stats");

 // Set the default parameters for style Nab_collaboration
 Nab_collaboration->SetCanvasBorderMode(0);     // Removes Canvas Border
 Nab_collaboration->SetPadBorderMode(0);        // Removes Pad Border
 Nab_collaboration->SetCanvasColor(0);          // Changes Canvas color to white
 Nab_collaboration->SetPadColor(0);             // Changes Pad color to white
 Nab_collaboration->SetStatColor(0);            // Changes Stats bg color to white
 Nab_collaboration->SetTitleFillColor(0);       // Changes Title bg color to white
 Nab_collaboration->SetLabelFont(42,"xyz");     // Changes Label Font
 Nab_collaboration->SetTitleFont(42,"xyz");     // Changes Axis Title Font
 Nab_collaboration->SetPadTickX(1);             // Sets tic marks on both horizontal axes
 Nab_collaboration->SetPadTickY(1);             // Sets tic marks on both vertical axes
 Nab_collaboration->SetTickLength(0.018,"xyz"); // Sets tic length
 Nab_collaboration->SetOptStat(0);              // Turns off Statistics display
 Nab_collaboration->SetOptTitle(0);             // Turns off Title display
 Nab_collaboration->SetHistLineWidth(2);        // Changes Histogram Line width
 Nab_collaboration->SetFrameBorderMode(0);      // Removes the Frame Border
 Nab_collaboration->SetFrameFillStyle(0);
 Nab_collaboration->SetCanvasDefH(494);         // Sets Default Canva Height
 Nab_collaboration->SetCanvasDefW(800);         // Sets Default Canvas Width
 Nab_collaboration->SetPalette(1);


 // The next for commands set the default margin size
 // n.b. the margins do not take axis labels into account! grr!!
 Nab_collaboration->SetPadTopMargin(0.1);     // Set Margin Top
 Nab_collaboration->SetPadRightMargin(0.1);   // Set Margin Right
 Nab_collaboration->SetPadBottomMargin(0.1);    // Set Margin Bottom
 Nab_collaboration->SetPadLeftMargin(0.1);     // Set Margin Left

 //make a nice palette
int NRGBs = 7, NCont = 999;
 Nab_collaboration->SetNumberContours(NCont);
 Double_t stops[7] = { 0.00, 0.10, 0.25, 0.45, 0.60, 0.75, 1.00 };
 Double_t red[7]   = { 1.00, 0.00, 0.00, 0.00, 0.97, 0.97, 0.10 };
 Double_t green[7] = { 1.00, 0.97, 0.30, 0.40, 0.97, 0.00, 0.00 };
 Double_t blue[7]  = { 1.00, 0.97, 0.97, 0.00, 0.00, 0.00, 0.00 };
 TColor::CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont);

 // Make Nab_collaboration_work a copy of Nab_collaboration and remove stats
 Nab_collaboration->Copy(*Nab_collaboration_work);
 Nab_collaboration_work->SetOptStat(1);
 Nab_collaboration_work->SetOptTitle(1);
 Nab_collaboration_work->SetPadTopMargin(0.1);
 Nab_collaboration_work->SetPadRightMargin(0.1);

 // Select Which Style to 
 gROOT->SetStyle("Nab_Collaboration_Work");
 // gROOT->SetStyle("Nab_Collaboration");


 // Use the RooFit functions
 // using namespace RooFit;

 // Force Root to run Nab_collaboration/Nab_collaboration_work style
 gROOT->ForceStyle();

}
