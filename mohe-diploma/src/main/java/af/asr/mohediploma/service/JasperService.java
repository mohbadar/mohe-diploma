package af.asr.mohediploma.service;

import af.asr.mohediploma.model.Certificate;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
import net.sf.jasperreports.engine.JasperReport;
import net.sf.jasperreports.engine.JRException;
import net.sf.jasperreports.engine.data.JRBeanArrayDataSource;
import net.sf.jasperreports.engine.data.JRBeanCollectionDataSource;

import net.sf.jasperreports.engine.data.JRBeanCollectionDataSource;
import net.sf.jasperreports.engine.export.JRPdfExporter;
import net.sf.jasperreports.export.SimpleExporterInput;
import net.sf.jasperreports.export.SimpleOutputStreamExporterOutput;
import net.sf.jasperreports.export.SimplePdfExporterConfiguration;
import net.sf.jasperreports.export.SimplePdfReportConfiguration;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;
import java.util.logging.Level;
import java.util.logging.Logger;

@Service
public class JasperService {

    public void printDiploma(Map<String, Object> params, String templatePath, List<Certificate> certificates, String outputFile) throws JRException {

        //1. Compile the report(.jrxml to .jasper) that we have designed using
        //Jaspersoft iReport Designer tool.
        JasperReport jasperReport = JasperCompileManager.compileReport(templatePath);

        //2.  Pass the list employees into JRBeanCollectionDataSource.
        JRBeanCollectionDataSource jrBeanCollectionDataSource = new JRBeanCollectionDataSource(certificates);

        //3.Fill the list of employee and parameters into the report by calling
        JasperPrint jasperPrint = JasperFillManager.fillReport(jasperReport,params,jrBeanCollectionDataSource);

        //4. Finally export the report to a PDF file.
        JasperExportManager.exportReportToPdfFile(jasperPrint, outputFile);
    }

//    public void exportToPdf(String fileName, String author) {
//
//        // print report to file
//        JRPdfExporter exporter = new JRPdfExporter();
//
//        exporter.setExporterInput(new SimpleExporterInput(jasperPrint));
//        exporter.setExporterOutput(new SimpleOutputStreamExporterOutput(fileName));
//
//        SimplePdfReportConfiguration reportConfig = new SimplePdfReportConfiguration();
//        reportConfig.setSizePageToContent(true);
//        reportConfig.setForceLineBreakPolicy(false);
//
//        SimplePdfExporterConfiguration exportConfig = new SimplePdfExporterConfiguration();
//        exportConfig.setMetadataAuthor(author);
//        exportConfig.setEncrypted(true);
//        exportConfig.setAllowedPermissionsHint("PRINTING");
////        exportConfig.
//
//        exporter.setConfiguration(reportConfig);
//        exporter.setConfiguration(exportConfig);
//        try {
//            exporter.exportReport();
//        } catch (JRException ex) {
//            Logger.getLogger(JasperService.class.getName()).log(Level.SEVERE, null, ex);
//        }
//    }
}
