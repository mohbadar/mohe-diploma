/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package af.asr.mohediploma.model;

import java.io.Serializable;
import java.util.Date;
import java.util.List;
import javax.persistence.Basic;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.NamedQueries;
import javax.persistence.NamedQuery;
import javax.persistence.OneToMany;
import javax.persistence.Table;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;

/**
 *
 * @author badar
 */
@Entity
@Table(name = "generic_certificate")
//@NamedQueries({
//    @NamedQuery(name = "GenericCertificate.findAll", query = "SELECT g FROM GenericCertificate g")})
public class Certificate implements Serializable {

    private static final long serialVersionUID = 1L;
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Basic(optional = false)
    @Column(name = "id")
    private Integer id;
    @Basic(optional = false)
    @Column(name = "firstname")
    private String firstname;
    @Basic(optional = false)
    @Column(name = "lastname")
    private String lastname;
    @Basic(optional = false)
    @Column(name = "fathername")
    private String fathername;
    @Basic(optional = false)
    @Column(name = "graduation_year")
    private int graduationYear;
    @Column(name = "slug")
    private String slug;
    @Basic(optional = false)
    @Column(name = "created_at")
    @Temporal(TemporalType.TIMESTAMP)
    private Date createdAt;
    @Basic(optional = false)
    @Column(name = "qrtext")
    private String qrtext;
    @Basic(optional = false)
    @Column(name = "degree_title")
    private String degreeTitle;
    @Basic(optional = false)
    @Column(name = "gender")
    private String gender;
    @Column(name = "picture")
    private String picture;
    @Basic(optional = false)
    @Column(name = "dob")
    @Temporal(TemporalType.DATE)
    private Date dob;
    @Basic(optional = false)
    @Column(name = "certificate_status")
    private String certificateStatus;
    @OneToMany(mappedBy = "certificateId")
    private List<Blankdiploma> blankdiplomaList;
    @JoinColumn(name = "user_id", referencedColumnName = "id")
    @ManyToOne
    private AuthUser userId;
    @JoinColumn(name = "department_id", referencedColumnName = "id")
    @ManyToOne(optional = false)
    private Department departmentId;

    public Certificate() {
    }

    public Certificate(Integer id) {
        this.id = id;
    }

    public Certificate(Integer id, String firstname, String lastname, String fathername, int graduationYear, Date createdAt, String qrtext, String degreeTitle, String gender, Date dob, String certificateStatus) {
        this.id = id;
        this.firstname = firstname;
        this.lastname = lastname;
        this.fathername = fathername;
        this.graduationYear = graduationYear;
        this.createdAt = createdAt;
        this.qrtext = qrtext;
        this.degreeTitle = degreeTitle;
        this.gender = gender;
        this.dob = dob;
        this.certificateStatus = certificateStatus;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public String getFathername() {
        return fathername;
    }

    public void setFathername(String fathername) {
        this.fathername = fathername;
    }

    public int getGraduationYear() {
        return graduationYear;
    }

    public void setGraduationYear(int graduationYear) {
        this.graduationYear = graduationYear;
    }

    public String getSlug() {
        return slug;
    }

    public void setSlug(String slug) {
        this.slug = slug;
    }

    public Date getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(Date createdAt) {
        this.createdAt = createdAt;
    }

    public String getQrtext() {
        return qrtext;
    }

    public void setQrtext(String qrtext) {
        this.qrtext = qrtext;
    }

    public String getDegreeTitle() {
        return degreeTitle;
    }

    public void setDegreeTitle(String degreeTitle) {
        this.degreeTitle = degreeTitle;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public String getPicture() {
        return picture;
    }

    public void setPicture(String picture) {
        this.picture = picture;
    }

    public Date getDob() {
        return dob;
    }

    public void setDob(Date dob) {
        this.dob = dob;
    }

    public String getCertificateStatus() {
        return certificateStatus;
    }

    public void setCertificateStatus(String certificateStatus) {
        this.certificateStatus = certificateStatus;
    }

    public List<Blankdiploma> getBlankdiplomaList() {
        return blankdiplomaList;
    }

    public void setBlankdiplomaList(List<Blankdiploma> blankdiplomaList) {
        this.blankdiplomaList = blankdiplomaList;
    }

    public AuthUser getUserId() {
        return userId;
    }

    public void setUserId(AuthUser userId) {
        this.userId = userId;
    }

    public Department getDepartmentId() {
        return departmentId;
    }

    public void setDepartmentId(Department departmentId) {
        this.departmentId = departmentId;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (id != null ? id.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof Certificate)) {
            return false;
        }
        Certificate other = (Certificate) object;
        if ((this.id == null && other.id != null) || (this.id != null && !this.id.equals(other.id))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "af.asr.mohediploma.model.GenericCertificate[ id=" + id + " ]";
    }
    
}
