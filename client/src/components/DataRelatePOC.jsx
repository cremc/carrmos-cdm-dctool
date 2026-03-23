import React, { useState, useCallback, useRef, useEffect } from 'react';
import axios from 'axios';
import {
    ReactFlow,
    useNodesState,
    useEdgesState,
    addEdge,
    Controls,
    Background,
    Handle,
    Position,
    MarkerType
} from '@xyflow/react';
import { Edit, ChevronRight, ChevronDown, Maximize2, Minimize2, RotateCcw } from 'lucide-react';
import SearchableDropdown from './SearchableDropdown';
import '@xyflow/react/dist/style.css';
import './DataRelatePOC.css';

// ------------------------------------------------------------------
// Helper functions for Data/Styling
// ------------------------------------------------------------------
const getStatusColor = (status) => {
    if (status === 'found') return '#a5d6a7'; // Decent Green
    if (status === 'not-found') return '#ef9a9a'; // Decent Light Red
    return '#949191ff'; // Default - Others
};

// ------------------------------------------------------------------
// Shared Context Menu Component
// ------------------------------------------------------------------
const NodeContextMenu = ({ menu, onClose, onAction }) => {
    if (!menu) return null;
    const { nodeData, top, left, type } = menu;

    const isGroupObj = type === 'group';

    if (isGroupObj) {
        return (
            <div className="context-menu" style={{ top, left }} onClick={(e) => e.stopPropagation()}>
                <div className="menu-item" onClick={() => { onAction('group_refresh', nodeData); onClose(); }}>
                    Refresh
                </div>
                <div className="menu-item" onClick={() => { onAction('group_refetch', nodeData); onClose(); }}>
                    Refetch
                </div>
            </div>
        );
    }

    // Disable DB fetches for red nodes
    const isGreen = nodeData.status === 'found';

    return (
        <div className="context-menu" style={{ top, left }} onClick={(e) => e.stopPropagation()}>
            <div
                className={`menu-item ${!isGreen ? 'disabled' : ''}`}
                onClick={() => { if (isGreen) { onAction('get_db', nodeData); onClose(); } }}
            >
                Get Requirements from db
            </div>
            <div className="menu-item" onClick={() => { onAction('get_ext', nodeData); onClose(); }}>
                Get Requirements from ext sources
            </div>
            <div className="menu-item" onClick={() => { onAction('get_all', nodeData); onClose(); }}>
                Get all Requirements
            </div>

            <div className="menu-separator"></div>

            <div className="menu-item" onClick={() => { onAction('details', nodeData); onClose(); }}>
                Show details...
            </div>
            <div className="menu-item" onClick={() => { onAction('toggle_ignore', nodeData); onClose(); }}>
                {nodeData.isIgnored ? 'Include' : 'Ignore'}
            </div>
            <div className="menu-item" onClick={() => { onAction('refresh', nodeData); onClose(); }}>
                Refresh
            </div>
        </div>
    );
};

// ------------------------------------------------------------------
// Standard Top-Level Career Position Node
// ------------------------------------------------------------------
const TopLevelCPNode = ({ data, id, isConnectable }) => {
    const bgColor = getStatusColor(data.status);

    return (
        <div className={`custom-node cp-node ${data.isIgnored ? 'ignored' : ''}`}
            style={{ backgroundColor: bgColor }}
            onContextMenu={(e) => data.onContextMenu(e, id, data, 'cp')}>
            <div className="cp-title">{data.label}</div>
            {data.exp && <div className="cp-exp">{data.exp}</div>}

            <Handle type="target" position={Position.Top} isConnectable={isConnectable} />
            <Handle type="source" id={id} position={Position.Bottom} isConnectable={isConnectable} />
        </div>
    );
};

// ------------------------------------------------------------------
// CertGroup Component (Handles vertical layout, AND/OR, and expand/collapse)
// ------------------------------------------------------------------
const CertGroup = ({ certsData, onContextMenu, id, isConnectable }) => {
    const [isExpanded, setIsExpanded] = useState(true);
    const hasMultiple = certsData.items.length > 1;
    const itemsToShow = isExpanded ? certsData.items : [certsData.items[0]];

    return (
        <div className="cert-group-container">
            {hasMultiple && (
                <button className="cert-group-toggle" onClick={() => setIsExpanded(!isExpanded)} title={isExpanded ? "Collapse" : "Expand"}>
                    {isExpanded ? <Minimize2 size={14} /> : <Maximize2 size={14} />}
                </button>
            )}
            <div className="cert-group-list">
                {itemsToShow.map((cert, index) => (
                    <React.Fragment key={cert.id}>
                        <div
                            className={`internal-node cert-node ${cert.isIgnored ? 'ignored' : ''}`}
                            style={{ '--node-bg': getStatusColor(cert.status) }}
                            onContextMenu={(e) => onContextMenu(e, id, cert, 'cert')}
                        >
                            <div className="node-title">{cert.label}</div>
                            <Handle type="source" id={cert.id} position={Position.Bottom} isConnectable={isConnectable} />
                        </div>
                        {isExpanded && index < itemsToShow.length - 1 && (
                            <div className="cert-operator-badge">{certsData.type || 'AND'}</div>
                        )}
                    </React.Fragment>
                ))}
            </div>
            {!isExpanded && hasMultiple && (
                <div className="cert-operator-badge" style={{ marginTop: '5px' }}>
                    + {certsData.items.length - 1} more ({certsData.type})
                </div>
            )}
        </div>
    );
};

// ------------------------------------------------------------------
// Sub-components for Group Node
// ------------------------------------------------------------------
const InternalCGNode = ({ cg, onContextMenu, id, isConnectable }) => {
    if (!cg) return null;
    return (
        <div className={`internal-node cg-node ${cg.isIgnored ? 'ignored' : ''}`}
            style={{ backgroundColor: getStatusColor(cg.status) }}
            onContextMenu={(e) => onContextMenu(e, id, cg, 'cg')}>
            <div className="node-title">{cg.label}</div>
            <Handle type="source" id={cg.id} position={Position.Bottom} isConnectable={isConnectable} />
        </div>
    );
};

const InternalCPNode = ({ cp, onContextMenu, id, isConnectable }) => {
    if (!cp) return null;
    return (
        <div className={`internal-node cp-node ${cp.isIgnored ? 'ignored' : ''}`}
            style={{ backgroundColor: getStatusColor(cp.status) }}
            onContextMenu={(e) => onContextMenu(e, id, cp, 'cp')}>
            <div className="cp-title">{cp.label}</div>
            <div className="cp-exp">{cp.exp}</div>
            <Handle type="source" id={cp.id} position={Position.Bottom} isConnectable={isConnectable} />
        </div>
    );
};

const InternalOthersGroup = ({ others, isConnectable }) => {
    const [isExpanded, setIsExpanded] = useState(false);
    if (!others || others.length === 0) return null;

    return (
        <div className="internal-others-series-container" style={{ position: 'relative' }}>
            <button 
                className="others-group-toggle" 
                onClick={(e) => { e.preventDefault(); e.stopPropagation(); setIsExpanded(!isExpanded); }} 
                title={isExpanded ? "Collapse" : "Expand"}
                style={{ position: 'absolute', top: -10, right: -10, zIndex: 10, background: '#fff', border: '1px solid #ccc', borderRadius: '50%', cursor: 'pointer', padding: 2 }}
            >
                {isExpanded ? <Minimize2 size={12} /> : <Maximize2 size={12} />}
            </button>
            {isExpanded ? (
                <div className="internal-others-series">
                    {others.map((oth, index) => (
                        <React.Fragment key={oth.id}>
                            <div className={`internal-node others-node ${oth.isIgnored ? 'ignored' : ''}`}
                                onContextMenu={(e) => { e.preventDefault(); e.stopPropagation(); }}>
                                <div className="node-title" style={{ position: 'relative', zIndex: 1, whiteSpace: 'nowrap', padding: '4px 8px', background: '#eee', borderRadius: '4px', border: '1px solid #ccc', fontSize: '11px' }}>
                                    {oth.category}: {oth.label}
                                </div>
                                <Handle type="source" id={oth.id} position={Position.Bottom} isConnectable={isConnectable} />
                            </div>
                            {index < others.length - 1 && <div className="series-connector-line" style={{ width: '1px', height: '10px', background: '#999', margin: '0 auto' }} />}
                        </React.Fragment>
                    ))}
                </div>
            ) : (
                <div className="internal-others-collapsed" style={{ margin: '5px 0', padding: '6px', background: '#e0e0e0', border: '1px solid #999', borderRadius: '4px', fontSize: '12px', textAlign: 'center', fontWeight: 'bold' }}>
                    Others
                    <div style={{ fontSize: '10px', fontWeight: 'normal', color: '#555', marginTop: '2px' }}>
                        {others.length} requirement sets
                    </div>
                </div>
            )}
        </div>
    );
};

// ------------------------------------------------------------------
// Group Node (Composite Container)
// ------------------------------------------------------------------
const GroupNode = ({ data, id, isConnectable }) => {
    const { pathName, cg, cp, certs, others, onContextMenu, filters } = data;

    return (
        <div className="group-node-container" onContextMenu={(e) => onContextMenu(e, id, data, 'group')}>
            <div className="group-node-label">{pathName}</div>

            {/* Target handle receives incoming edges from parent nodes */}
            <Handle type="target" position={Position.Top} isConnectable={isConnectable} />

            <div className="group-internal-layout">

                {/* 1. Course General */}
                {filters.academic && <InternalCGNode cg={cg} onContextMenu={onContextMenu} id={id} isConnectable={isConnectable} />}

                {/* 2. Career Position */}
                {filters.workEx && <InternalCPNode cp={cp} onContextMenu={onContextMenu} id={id} isConnectable={isConnectable} />}

                {/* 3. Certifications (Vertical Layout with AND/OR) */}
                {certs && certs.items && certs.items.length > 0 && filters.certification && (
                    <CertGroup certsData={certs} onContextMenu={onContextMenu} id={id} isConnectable={isConnectable} />
                )}

                {/* 4. Others (Series) */}
                {filters.others && <InternalOthersGroup others={others} isConnectable={isConnectable} />}

            </div>
        </div>
    );
};


const nodeTypes = {
    topCP: TopLevelCPNode,
    groupNode: GroupNode
};

// ------------------------------------------------------------------
// Extended Top-Level Node Rendering for different types
// ------------------------------------------------------------------
const StartingNode = ({ data, id, isConnectable }) => {
    const bgColor = getStatusColor(data.status);

    // Fallback to CP style if type is missing
    const nodeType = data.type || 'cp';
    const isCP = nodeType === 'cp';
    const isCG = nodeType === 'cg';
    const isCert = nodeType === 'cert';

    // Choose CSS class based on node type
    let nodeClass = 'cp-node';
    if (isCG) nodeClass = 'cg-node internal-node';
    if (isCert) nodeClass = 'cert-node-starting internal-node';

    return (
        <div className={`custom-node ${nodeClass} ${data.isIgnored ? 'ignored' : ''}`}
            style={{
                backgroundColor: isCert ? 'transparent' : bgColor,
                '--node-bg': bgColor,
                color: 'black',
                fontWeight: 'bold',
                cursor: 'pointer'
            }}
            onContextMenu={(e) => data.onContextMenu(e, id, data, nodeType)}>
            <div className={isCP ? "cp-title" : "node-title"}>{data.label}</div>
            {isCP && data.exp && <div className="cp-exp">{data.exp}</div>}

            <Handle type="target" position={Position.Top} isConnectable={isConnectable} />
            <Handle type="source" id={id} position={Position.Bottom} isConnectable={isConnectable} />
        </div>
    );
};

nodeTypes.startingNode = StartingNode;

// ------------------------------------------------------------------
// Mock Data for progressive cascading filters
// ------------------------------------------------------------------
const mockCPData = {
    industries: [{ value: 'ind1', label: 'Technology' }, { value: 'ind2', label: 'Finance' }],
    branches: [
        { value: 'br1', label: 'Software Development', parent: 'ind1' },
        { value: 'br2', label: 'Data Science', parent: 'ind1' },
        { value: 'br3', label: 'Investment Banking', parent: 'ind2' }
    ],
    cps: [
        { value: 'cp1', label: 'Frontend Engineer', parent: 'br1' },
        { value: 'cp2', label: 'Backend Engineer', parent: 'br1' },
        { value: 'cp3', label: 'Data Analyst', parent: 'br2' },
        { value: 'cp4', label: 'Portfolio Manager', parent: 'br3' }
    ]
};

const mockCGData = {
    acadLevels: [{ value: 'ac1', label: 'Undergraduate' }, { value: 'ac2', label: 'Postgraduate' }],
    discGroups: [{ value: 'dg1', label: 'Engineering' }, { value: 'dg2', label: 'Business' }],
    disciplines: [
        { value: 'd1', label: 'Computer Science', parent: 'dg1' },
        { value: 'd2', label: 'Mechanical', parent: 'dg1' },
        { value: 'd3', label: 'Management', parent: 'dg2' }
    ],
    cgs: [
        { value: 'cg1', label: 'B.Tech CS', parent: 'd1', acad: 'ac1' },
        { value: 'cg2', label: 'M.Tech CS', parent: 'd1', acad: 'ac2' },
        { value: 'cg3', label: 'B.E. Mechanical', parent: 'd2', acad: 'ac1' },
        { value: 'cg4', label: 'MBA', parent: 'd3', acad: 'ac2' }
    ]
};

const mockCertData = {
    types: [{ value: 't1', label: 'Professional' }, { value: 't2', label: 'Vendor Specific' }],
    domains: [
        { value: 'dom1', label: 'Cloud Computing', parent: 't1' },
        { value: 'dom2', label: 'Networking', parent: 't2' }
    ],
    certs: [
        { value: 'c1', label: 'AWS Certified Solutions Architect', parent: 'dom1' },
        { value: 'c2', label: 'Azure Administrator', parent: 'dom1' },
        { value: 'c3', label: 'CCNA', parent: 'dom2' }
    ]
};

// ------------------------------------------------------------------
// Main POC Application / Component
// ------------------------------------------------------------------
export default function DataRelatePOC() {
    const reactFlowWrapper = useRef(null);
    const [menu, setMenu] = useState(null);
    const [modalData, setModalData] = useState(null);
    const [promptModalOpen, setPromptModalOpen] = useState(false);
    const [promptText, setPromptText] = useState("Extract academic courses, certifications, work experience, and skills required for the given career position.");
    const [isControlsOpen, setIsControlsOpen] = useState(true);

    // Top Level Selector State
    const [selectorOpen, setSelectorOpen] = useState(false);
    const [selectorMode, setSelectorMode] = useState('cp'); // 'cp', 'cg', 'cert'
    const [cpForm, setCpForm] = useState({ ind: null, branch: null, cp: null });
    const [cgForm, setCgForm] = useState({ acad: null, dg: null, disc: null, cg: null });
    const [certForm, setCertForm] = useState({ type: null, domain: null, cert: null });

    const [filters, setFilters] = useState({
        academic: true,
        workEx: true,
        certification: true,
        others: true
    });

    const handleClearForm = () => {
        setCpForm({ ind: null, branch: null, cp: null });
        setCgForm({ acad: null, dg: null, disc: null, cg: null });
        setCertForm({ type: null, domain: null, cert: null });
    };

    const handleCancelForm = () => {
        setSelectorOpen(false);
    };

    const handleOkForm = () => {
        const hasExpandedNodes = nodes.length > 1;
        let selectedItem = null;
        let label = '';
        if (selectorMode === 'cp') {
            selectedItem = cpForm.cp;
            label = selectedItem?.label;
        } else if (selectorMode === 'cg') {
            selectedItem = cgForm.cg;
            label = selectedItem?.label;
        } else if (selectorMode === 'cert') {
            selectedItem = certForm.cert;
            label = selectedItem?.label;
        }

        if (!selectedItem) return;

        if (hasExpandedNodes) {
            const proceed = window.confirm("Warning: Changing the Starting Node at this point may result in losing unsaved data. Do you want to proceed?");
            if (!proceed) return;
        }

        const newNodes = [
            {
                id: `top-${selectorMode}-${Date.now()}`,
                type: 'startingNode',
                position: { x: 400, y: 50 },
                data: { label: label, status: 'found', isIgnored: false, onContextMenu: handleContextMenu, type: selectorMode },
            }
        ];

        setNodes(newNodes);
        setEdges([]);
        setSelectorOpen(false);
    };

    const isOkDisabled = () => {
        if (selectorMode === 'cp') return !cpForm.cp;
        if (selectorMode === 'cg') return !cgForm.cg;
        if (selectorMode === 'cert') return !certForm.cert;
        return true;
    };

    // Handle Context Menu triggers
    const handleContextMenu = useCallback((event, groupId, itemData, type) => {
        event.preventDefault();
        event.stopPropagation();
        const bounds = reactFlowWrapper.current.getBoundingClientRect();
        setMenu({
            groupId,
            nodeData: itemData,
            type,
            top: event.clientY - bounds.top,
            left: event.clientX - bounds.left,
        });
    }, []);

    const closeMenu = useCallback(() => setMenu(null), []);

    const handleMenuAction = useCallback((action, nodeData) => {
        if (action === 'details') {
            setModalData(nodeData);
        } else if (action === 'toggle_ignore') {
            setNodes((nds) => {
                return nds.map((n) => {
                    if (n.type === 'topCP' && n.id === nodeData.id) {
                        return { ...n, data: { ...n.data, isIgnored: !n.data.isIgnored } };
                    }
                    if (n.type === 'groupNode') {
                        const newData = { ...n.data };
                        if (newData.cg && newData.cg.id === nodeData.id) newData.cg.isIgnored = !newData.cg.isIgnored;
                        if (newData.cp && newData.cp.id === nodeData.id) newData.cp.isIgnored = !newData.cp.isIgnored;
                        if (newData.certs && newData.certs.items) {
                            newData.certs.items = newData.certs.items.map(c => c.id === nodeData.id ? { ...c, isIgnored: !c.isIgnored } : c);
                        }
                        if (newData.others) {
                            newData.others = newData.others.map(o => o.id === nodeData.id ? { ...o, isIgnored: !o.isIgnored } : o);
                        }
                        return { ...n, data: newData };
                    }
                    return n;
                });
            });
        } else if (action === 'refresh') {
            // Mock toggle status
            setNodes((nds) => {
                return nds.map((n) => {
                    const toggleStatus = (status) => status === 'found' ? 'not-found' : 'found';

                    if (n.type === 'topCP' && n.id === nodeData.id) {
                        return { ...n, data: { ...n.data, status: toggleStatus(n.data.status) } };
                    }
                    if (n.type === 'groupNode') {
                        const newData = { ...n.data };
                        if (newData.cg && newData.cg.id === nodeData.id) newData.cg.status = toggleStatus(newData.cg.status);
                        if (newData.cp && newData.cp.id === nodeData.id) newData.cp.status = toggleStatus(newData.cp.status);
                        if (newData.certs && newData.certs.items) {
                            newData.certs.items = newData.certs.items.map(c => c.id === nodeData.id ? { ...c, status: toggleStatus(c.status) } : c);
                        }
                        return { ...n, data: newData };
                    }
                    return n;
                });
            });
        } else if (action === 'get_ext') {
            alert(`Fetching requirements via LLM for: ${nodeData.label}`);
            
            const domainMap = { 'cp': 'career_position', 'cg': 'course_general' };
            const reqDomain = domainMap[menu.type] || 'course_general';

            axios.post('http://localhost:8000/api/pe/datarelate/run', {
                domain: reqDomain,
                input_data: { label: nodeData.label }
            }).then((response) => {
                const fetchedGroups = response.data.results || [];
                const newNodes = [];
                const newEdges = [];

                fetchedGroups.forEach((group, index) => {
                    const newGroupId = `group-ext-${Date.now()}-${index}`;

                    // Mock function to check if item exists in DB
                    const checkDbMock = (label) => Math.random() > 0.5 ? 'found' : 'not-found';

                    const cgVal = group.data.cg;
                    let cgLabel = typeof cgVal === 'string' ? cgVal : (cgVal?.label || '');
                    const cg = cgVal ? { id: `cg-${newGroupId}`, label: cgLabel, status: checkDbMock(cgLabel), isIgnored: false } : null;

                    const cpVal = group.data.cp;
                    let cpLabel = typeof cpVal === 'string' ? cpVal : (cpVal?.label || '');
                    let cpExp = typeof cpVal === 'object' ? (cpVal?.exp || '') : '';
                    const cp = cpVal ? { id: `cp-${newGroupId}`, label: cpLabel, exp: cpExp, status: checkDbMock(cpLabel), isIgnored: false } : null;
                    
                    let certGroupData = { type: 'AND', items: [] };
                    if (group.data.certs && group.data.certs.length > 0) {
                        const firstCertSet = group.data.certs.find(c => c.anded_certs?.length > 0 || c.ored_certs?.length > 0) || group.data.certs[0];
                        certGroupData.type = firstCertSet.type;
                        if (firstCertSet.type === 'AND' && firstCertSet.anded_certs) {
                            certGroupData.items = firstCertSet.anded_certs.map((c, i) => {
                                const l = typeof c === 'string' ? c : (c.label || '');
                                return { id: `cert-${newGroupId}-${i}`, label: l, status: checkDbMock(l), isIgnored: false };
                            });
                        } else if (firstCertSet.type === 'OR' && firstCertSet.ored_certs) {
                            certGroupData.items = firstCertSet.ored_certs.map((c, i) => {
                                const l = typeof c === 'string' ? c : (c.label || '');
                                return { id: `cert-${newGroupId}-${i}`, label: l, status: checkDbMock(l), isIgnored: false };
                            });
                        }
                    }

                    const othersList = [];
                    const dOthers = group.data.others || {};
                    if (dOthers.skills && dOthers.skills.length > 0) {
                         const str = dOthers.skills.map(s => typeof s === 'string' ? s : (s.skill_subcategory || s.skill_category || '')).join(', ');
                         othersList.push({ id: `sk-${newGroupId}`, category: 'Skills', label: str, isIgnored: false });
                    }
                    if (dOthers.subjects && dOthers.subjects.length > 0) {
                         const str = dOthers.subjects.map(s => typeof s === 'string' ? s : (s.subject_name || '')).join(', ');
                         othersList.push({ id: `su-${newGroupId}`, category: 'Subjects', label: str, isIgnored: false });
                    }
                    if (dOthers.ET && dOthers.ET !== 'none') {
                         othersList.push({ id: `et-${newGroupId}`, category: 'ETs', label: dOthers.ET, isIgnored: false });
                    }
                    if (dOthers.other_reqs && dOthers.other_reqs.length > 0) {
                         const count = dOthers.other_reqs.reduce((acc, reqGroup) => 
                             acc + (reqGroup.anded_other_reqs?.length || 0) + (reqGroup.ored_other_reqs?.length || 0)
                         , 0) || dOthers.other_reqs.length;
                         othersList.push({ id: `or-${newGroupId}`, category: 'Other Reqs', label: count + ' requirements', isIgnored: false });
                    }

                    const newNode = {
                        id: newGroupId,
                        type: 'groupNode',
                        position: { x: 100 + index * 300, y: Math.random() * 100 + 500 },
                        data: {
                            pathName: group.data.pathName || `Path ${index + 1}`,
                            cg,
                            cp,
                            certs: certGroupData,
                            others: othersList,
                            onContextMenu: handleContextMenu,
                            filters // will sync via useEffect, but provide initial
                        }
                    };

                    const newEdge = {
                        id: `e-${nodeData.id}-${newGroupId}`,
                        source: menu.groupId || nodeData.id,
                        sourceHandle: nodeData.id,
                        target: newGroupId,
                        type: 'smoothstep',
                        markerEnd: { type: MarkerType.ArrowClosed, orient: 'auto-start-reverse' },
                        style: { strokeWidth: 2, stroke: '#555' }
                    };

                    newNodes.push(newNode);
                    newEdges.push(newEdge);
                });

                setNodes((nds) => [...nds, ...newNodes]);
                setEdges((eds) => [...eds, ...newEdges]);
            }).catch(err => {
                console.error("Failed to fetch data from API", err);
                alert("Failed to fetch generated requirements from API. Check console.");
            });
            
        } else if (action.startsWith('get_')) {
            // Mock spawning new groups from this node
            const fetchType = action === 'get_db' ? 'Local DB' : 'Local + LLM';
            alert(`Fetching requirements via ${fetchType} for: ${nodeData.label}`);

            const newGroupId = `group-${Date.now()}`;
            const newNode = {
                id: newGroupId,
                type: 'groupNode',
                position: { x: Math.random() * 400, y: Math.random() * 200 + 400 },
                data: {
                    pathName: `New Path from ${nodeData.label}`,
                    cg: { id: `cg-${Date.now()}`, label: 'New Academic', status: 'found', isIgnored: false },
                    cp: null,
                    certs: { type: 'AND', items: [] },
                    others: [{ id: `oth-${Date.now()}`, category: 'Skills', label: 'New Skill', isIgnored: false }],
                    onContextMenu: handleContextMenu,
                    filters 
                }
            };

            const newEdge = {
                id: `e-${nodeData.id}-${newGroupId}`,
                source: menu.groupId || nodeData.id, 
                sourceHandle: nodeData.id,
                target: newGroupId,
                type: 'smoothstep',
                markerEnd: { type: MarkerType.ArrowClosed, orient: 'auto-start-reverse' },
                style: { strokeWidth: 2, stroke: '#555' }
            };

            setNodes((nds) => [...nds, newNode]);
            setEdges((eds) => [...eds, newEdge]);
        }
    }, [menu, handleContextMenu, filters]); // Added filters to deps since we use it

    // Initial Mock Data 
    const initialNodes = [
        {
            id: 'top-cp', type: 'startingNode', position: { x: 400, y: 50 },
            data: { label: 'Investment Banker', status: 'found', isIgnored: false, onContextMenu: handleContextMenu, type: 'cp' },
        },
        {
            id: 'group-1', type: 'groupNode', position: { x: 100, y: 200 },
            data: {
                pathName: 'Path 1',
                cg: { id: 'cg-1', label: 'MBA - Finance', status: 'found', isIgnored: false },
                cp: { id: 'cp-1', label: 'Portfolio Manager', exp: '3 Years', status: 'not-found', isIgnored: false },
                certs: { type: 'OR', items: [] },
                others: [
                    { id: 'oth-1', category: 'Skills', label: 'Financial Investments', isIgnored: false },
                    { id: 'oth-2', category: 'Skills', label: 'IPOs', isIgnored: false }
                ],
                onContextMenu: handleContextMenu,
                filters
            }
        },
        {
            id: 'group-2', type: 'groupNode', position: { x: 700, y: 200 },
            data: {
                pathName: 'Path 2',
                cg: { id: 'cg-2', label: 'Chartered Accountant (CA)', status: 'found', isIgnored: false },
                cp: { id: 'cp-2', label: 'Corp Accounts Consultant', exp: '2 Years', status: 'found', isIgnored: false },
                certs: {
                    type: 'AND',
                    items: [
                        { id: 'cert-1', label: 'CFA L1', status: 'not-found', isIgnored: false },
                        { id: 'cert-2', label: 'CFA L2', status: 'not-found', isIgnored: false }
                    ]
                },
                others: [
                    { id: 'oth-3', category: 'Skills', label: 'M&As', isIgnored: false }
                ],
                onContextMenu: handleContextMenu,
                filters
            }
        }
    ];

    const defaultEdgeOptions = {
        type: 'smoothstep',
        markerEnd: { type: MarkerType.ArrowClosed, orient: 'auto-start-reverse' },
        style: { strokeWidth: 2, stroke: '#555' }
    };

    const initialEdges = [
        { id: 'e1', source: 'top-cp', sourceHandle: 'top-cp', target: 'group-1', ...defaultEdgeOptions },
        { id: 'e2', source: 'top-cp', sourceHandle: 'top-cp', target: 'group-2', ...defaultEdgeOptions },
    ];

    const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
    const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

    // Sync filters to nodes cleanly
    useEffect(() => {
        setNodes((nds) => nds.map(n => {
            if (n.type === 'groupNode') {
                return { ...n, data: { ...n.data, filters } };
            }
            return n;
        }));
    }, [filters, setNodes]);

    const onConnect = useCallback((params) => setEdges((eds) => addEdge({ ...params, ...defaultEdgeOptions }, eds)), [setEdges, defaultEdgeOptions]);

    return (
        <div className="react-flow-wrapper" ref={reactFlowWrapper} onClick={closeMenu}>

            {/* Top Left: Top Level Node Selector Panel */}
            <div className="top-level-selector-panel" onClick={(e) => e.stopPropagation()}>
                <button
                    className="selector-toggle-btn"
                    onClick={() => setSelectorOpen(!selectorOpen)}
                    title="Toggle Top Level Node Selector"
                >
                    <ChevronRight
                        size={18}
                        style={{ transform: selectorOpen ? 'rotate(180deg)' : 'rotate(0deg)', transition: 'transform 0.3s' }}
                    />
                </button>
                <div className={`selector-panel-content ${selectorOpen ? 'open' : 'collapsed'}`}>
                    <div className="selector-panel-header">Starting Node</div>

                    {/* Radio Options */}
                    <div className="radio-group">
                        <label className="radio-label">
                            <input type="radio" name="topNodeMode" checked={selectorMode === 'cp'} onChange={() => setSelectorMode('cp')} /> Career Position
                        </label>
                        <label className="radio-label">
                            <input type="radio" name="topNodeMode" checked={selectorMode === 'cg'} onChange={() => setSelectorMode('cg')} /> Course General
                        </label>
                        <label className="radio-label">
                            <input type="radio" name="topNodeMode" checked={selectorMode === 'cert'} onChange={() => setSelectorMode('cert')} /> Certification
                        </label>
                    </div>

                    {/* Cascading Dropdowns Wrapper */}
                    <div className="dropdown-cascade-container">
                        {selectorMode === 'cp' && (
                            <>
                                <SearchableDropdown
                                    placeholder="Industry"
                                    options={mockCPData.industries}
                                    value={cpForm.ind}
                                    onChange={(val) => setCpForm({ ...cpForm, ind: val, branch: null, cp: null })}
                                />
                                <SearchableDropdown
                                    placeholder="Industry Branch"
                                    options={cpForm.ind ? mockCPData.branches.filter(b => b.parent === cpForm.ind.value) : mockCPData.branches}
                                    value={cpForm.branch}
                                    onChange={(val) => setCpForm({ ...cpForm, branch: val, cp: null })}
                                />
                                <SearchableDropdown
                                    placeholder="Career Position"
                                    options={
                                        cpForm.branch
                                            ? mockCPData.cps.filter(c => c.parent === cpForm.branch.value)
                                            : cpForm.ind
                                                ? mockCPData.cps.filter(c => mockCPData.branches.filter(b => b.parent === cpForm.ind.value).map(b => b.value).includes(c.parent))
                                                : mockCPData.cps
                                    }
                                    value={cpForm.cp}
                                    onChange={(val) => setCpForm({ ...cpForm, cp: val })}
                                />
                            </>
                        )}

                        {selectorMode === 'cg' && (
                            <>
                                <SearchableDropdown
                                    placeholder="Academic Level"
                                    options={mockCGData.acadLevels}
                                    value={cgForm.acad}
                                    onChange={(val) => setCgForm({ ...cgForm, acad: val })}
                                />
                                <SearchableDropdown
                                    placeholder="Discipline Group"
                                    options={mockCGData.discGroups}
                                    value={cgForm.dg}
                                    onChange={(val) => setCgForm({ ...cgForm, dg: val, disc: null, cg: null })}
                                />
                                <SearchableDropdown
                                    placeholder="Discipline"
                                    options={cgForm.dg ? mockCGData.disciplines.filter(d => d.parent === cgForm.dg.value) : mockCGData.disciplines}
                                    value={cgForm.disc}
                                    onChange={(val) => setCgForm({ ...cgForm, disc: val, cg: null })}
                                />
                                <SearchableDropdown
                                    placeholder="Course General"
                                    options={
                                        (cgForm.disc
                                            ? mockCGData.cgs.filter(c => c.parent === cgForm.disc.value)
                                            : cgForm.dg
                                                ? mockCGData.cgs.filter(c => mockCGData.disciplines.filter(d => d.parent === cgForm.dg.value).map(d => d.value).includes(c.parent))
                                                : mockCGData.cgs
                                        ).filter(c => cgForm.acad ? c.acad === cgForm.acad.value : true)
                                    }
                                    value={cgForm.cg}
                                    onChange={(val) => setCgForm({ ...cgForm, cg: val })}
                                />
                            </>
                        )}

                        {selectorMode === 'cert' && (
                            <>
                                <SearchableDropdown
                                    placeholder="Certification Type"
                                    options={mockCertData.types}
                                    value={certForm.type}
                                    onChange={(val) => setCertForm({ ...certForm, type: val, domain: null, cert: null })}
                                />
                                <SearchableDropdown
                                    placeholder="Domain"
                                    options={certForm.type ? mockCertData.domains.filter(d => d.parent === certForm.type.value) : mockCertData.domains}
                                    value={certForm.domain}
                                    onChange={(val) => setCertForm({ ...certForm, domain: val, cert: null })}
                                />
                                <SearchableDropdown
                                    placeholder="Certification"
                                    options={
                                        certForm.domain
                                            ? mockCertData.certs.filter(c => c.parent === certForm.domain.value)
                                            : certForm.type
                                                ? mockCertData.certs.filter(c => mockCertData.domains.filter(d => d.parent === certForm.type.value).map(d => d.value).includes(c.parent))
                                                : mockCertData.certs
                                    }
                                    value={certForm.cert}
                                    onChange={(val) => setCertForm({ ...certForm, cert: val })}
                                />
                            </>
                        )}
                    </div>

                    {/* Action Panel */}
                    <div className="selector-panel-actions">
                        <button className="clear-btn" onClick={handleClearForm} title="Clear form">
                            <RotateCcw size={16} />
                        </button>
                        <div className="right-actions">
                            <button className="cancel-btn" onClick={handleCancelForm}>Cancel</button>
                            <button className="ok-btn" onClick={handleOkForm} disabled={isOkDisabled()}>OK</button>
                        </div>
                    </div>
                </div>
            </div>

            {/* Top Right Controls Overlay */}
            <div className="datarelate-controls" onClick={(e) => e.stopPropagation()} style={{ background: 'white', padding: '10px', border: '1px solid #ccc', borderRadius: '4px', minWidth: '150px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', cursor: 'pointer', marginBottom: isControlsOpen ? '10px' : '0' }} onClick={() => setIsControlsOpen(!isControlsOpen)}>
                    <strong style={{ fontSize: '14px', marginRight: '10px' }}>Settings</strong>
                    {isControlsOpen ? <ChevronDown size={14} /> : <ChevronRight size={14} />}
                </div>

                {isControlsOpen && (
                    <>
                        <button className="edit-prompt-btn" onClick={() => setPromptModalOpen(true)} style={{ width: '100%', marginBottom: '10px' }}>
                            <Edit size={16} /> Edit prompt
                        </button>
                        <div className="display-filters">
                            <h4 style={{ marginTop: '5px', marginBottom: '8px', fontSize: '13px' }}>Display Layers</h4>
                            <label className="filter-label">
                                <input type="checkbox" checked={filters.academic} onChange={(e) => setFilters(f => ({ ...f, academic: e.target.checked }))} /> Academic
                            </label>
                            <label className="filter-label">
                                <input type="checkbox" checked={filters.workEx} onChange={(e) => setFilters(f => ({ ...f, workEx: e.target.checked }))} /> Work Ex
                            </label>
                            <label className="filter-label">
                                <input type="checkbox" checked={filters.certification} onChange={(e) => setFilters(f => ({ ...f, certification: e.target.checked }))} /> Certification
                            </label>
                            <label className="filter-label">
                                <input type="checkbox" checked={filters.others} onChange={(e) => setFilters(f => ({ ...f, others: e.target.checked }))} /> Others
                            </label>
                        </div>
                    </>
                )}
            </div>

            <ReactFlow
                nodes={nodes}
                edges={edges}
                onNodesChange={onNodesChange}
                onEdgesChange={onEdgesChange}
                onConnect={onConnect}
                nodeTypes={nodeTypes}
                fitView
            >
                <Background color="#ccc" gap={16} />
                <Controls />
            </ReactFlow>

            {/* Context Menu Render */}
            <NodeContextMenu menu={menu} onClose={closeMenu} onAction={handleMenuAction} />

            {/* Detail Modal */}
            {modalData && (
                <div className="poc-modal-overlay" onClick={() => setModalData(null)}>
                    <div className="poc-modal" onClick={e => e.stopPropagation()}>
                        <h3>Details: {modalData.label}</h3>
                        <table className="modal-table">
                            <tbody>
                                {modalData.exp && <tr><td><strong>Experience</strong></td><td>{modalData.exp}</td></tr>}
                                {modalData.category && <tr><td><strong>Category</strong></td><td>{modalData.category}</td></tr>}
                                <tr><td><strong>Status</strong></td><td>{modalData.status === 'found' ? 'Found in DB (Green)' : modalData.status === 'not-found' ? 'Missing in DB (Red)' : 'N/A'}</td></tr>
                            </tbody>
                        </table>

                        <div className="modal-footer">
                            <button onClick={() => setModalData(null)}>Close</button>
                        </div>
                    </div>
                </div>
            )}

            {/* Edit Prompt Modal */}
            {promptModalOpen && (
                <div className="poc-modal-overlay">
                    <div className="poc-modal prompt-editor" style={{ width: '400px' }}>
                        <h3>Edit System Prompt</h3>
                        <textarea
                            value={promptText}
                            onChange={(e) => setPromptText(e.target.value)}
                        />
                        <div className="modal-footer">
                            <button onClick={() => setPromptModalOpen(false)}>Cancel</button>
                            <button className="primary-btn" onClick={() => { alert('Prompt Saved!'); setPromptModalOpen(false); }}>Save</button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}
