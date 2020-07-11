/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package af.asr.mohediploma.model;

import java.io.Serializable;
import java.util.List;
import javax.persistence.Basic;
import javax.persistence.CascadeType;
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

/**
 *
 * @author badar
 */
@Entity
@Table(name = "auth_permission")
//@NamedQueries({
//    @NamedQuery(name = "AuthPermission.findAll", query = "SELECT a FROM AuthPermission a")})
public class AuthPermission implements Serializable {

    private static final long serialVersionUID = 1L;
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Basic(optional = false)
    @Column(name = "id")
    private Integer id;
    @Basic(optional = false)
    @Column(name = "name")
    private String name;
    @Basic(optional = false)
    @Column(name = "codename")
    private String codename;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "permissionId")
    private List<AuthUserUserPermissions> authUserUserPermissionsList;
    @JoinColumn(name = "content_type_id", referencedColumnName = "id")
    @ManyToOne(optional = false)
    private DjangoContentType contentTypeId;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "permissionId")
    private List<AuthGroupPermissions> authGroupPermissionsList;

    public AuthPermission() {
    }

    public AuthPermission(Integer id) {
        this.id = id;
    }

    public AuthPermission(Integer id, String name, String codename) {
        this.id = id;
        this.name = name;
        this.codename = codename;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCodename() {
        return codename;
    }

    public void setCodename(String codename) {
        this.codename = codename;
    }

    public List<AuthUserUserPermissions> getAuthUserUserPermissionsList() {
        return authUserUserPermissionsList;
    }

    public void setAuthUserUserPermissionsList(List<AuthUserUserPermissions> authUserUserPermissionsList) {
        this.authUserUserPermissionsList = authUserUserPermissionsList;
    }

    public DjangoContentType getContentTypeId() {
        return contentTypeId;
    }

    public void setContentTypeId(DjangoContentType contentTypeId) {
        this.contentTypeId = contentTypeId;
    }

    public List<AuthGroupPermissions> getAuthGroupPermissionsList() {
        return authGroupPermissionsList;
    }

    public void setAuthGroupPermissionsList(List<AuthGroupPermissions> authGroupPermissionsList) {
        this.authGroupPermissionsList = authGroupPermissionsList;
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
        if (!(object instanceof AuthPermission)) {
            return false;
        }
        AuthPermission other = (AuthPermission) object;
        if ((this.id == null && other.id != null) || (this.id != null && !this.id.equals(other.id))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "af.asr.mohediploma.model.AuthPermission[ id=" + id + " ]";
    }
    
}
